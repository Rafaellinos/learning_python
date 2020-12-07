from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from main.models import Flight
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def homepage(request):
    return render(request, "main/index.html", context={"flights": Flight.objects.all()})  # ./templates/main/index.html

def flight(request, id):
    # try:
    #     flight = Flight.objects.get(pk=id)
    # except ObjectDoesNotExist:
    #     raise Http404("Flight does not exist")
    flight = get_object_or_404(Flight, pk=id)  # mesma coisa que acima
    return render(request, "main/index.html", context={"flights": [flight]})
