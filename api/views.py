from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from rest_framework.parsers import JSONParser
from task.models import Task


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List/': '/task-list/',
        'Detail View': 'task-detail/<int:pk>',
        'Create': 'task-create/',
        'Update': 'task-update/<int:pk>',
        'Delete': 'task-delete/<int:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def taskUpdate(request ,pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        serializer = TaskSerializers(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
    else:
        serializer = TaskSerializers(instance=task)
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return Response("ITem successfully delete.")
