from django import forms
from .models import Task

# class TaskForm(forms.ModelForm):
#     title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new Task...'}))
#     class Meta:
#         model = Task
#         fields = '__all__'


class UpdateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "new-item", "placeholder": "New Item"}), required=False)
    class Meta:
        model = Task
        fields = ['title']
