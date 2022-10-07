from django.shortcuts import render
from .models import Person
# Create your views here.



def index(request):
    data = {'people': Person.objects.all()}
    return render(request, 'home/index.html', data)