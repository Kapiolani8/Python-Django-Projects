from django.shortcuts import render
from datetime import datetime


def index(request):
    context={
        "time": datetime.now()
    }
    return render(request, "time_display/index.html", context)

