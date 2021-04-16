from django.shortcuts import render
from django.http import request

import datetime

now = datetime.datetime.now()
month = now.month
day = now.day

if month == 1 and day == 1 :
    isNewYear = 'Yes'
else :
    isNewYear = 'No'


# Create your views here.


def index(request):
    return render(request, 'index.html', {
        "newYear" : isNewYear
    })
