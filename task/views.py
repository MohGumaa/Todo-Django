import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import UpdateForm

def home(request):

    if request.method == 'POST':
        u_form = UpdateForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            return redirect('home')
    else:
     u_form = UpdateForm()

    context = {
        "title": "Today",
        "tasks": Task.objects.all(),
        "u_form": u_form,
        "today_date": datetime.datetime.now()
    }
    return render(request, 'task/list.html', context)

def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('home')

