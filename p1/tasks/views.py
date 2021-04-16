from django.shortcuts import render

tasks = ['foo', 'bar', 'baz']
# Create your views here.


def home(request):
    return render(request, 'tasks/index.html', {
        'tasks' : tasks
    })


def add(request):
    return render(request, 'tasks/add/index.html')