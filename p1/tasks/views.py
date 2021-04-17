from django import forms
from django.shortcuts import render

tasks = ['foo', 'bar', 'baz']

class NewTaskForm(forms.Form):
    task_name = forms.CharField(label='task name')

def home(request):
    return render(request, 'tasks/index.html', {
        'tasks' : tasks
    })


def add(request):
    return render(request, 'tasks/add/add.html', {
        'form' : NewTaskForm()
    })

