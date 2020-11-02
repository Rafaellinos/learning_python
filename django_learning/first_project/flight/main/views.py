from django.shortcuts import render
from django.http import HttpResponse
from main.models import Flight


# Create your views here.

def homepage(request):
    return render(request, "main/index.html", context={"flights": Flight.objects.all()})  # ./templates/main/index.html
