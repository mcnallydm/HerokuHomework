from django.shortcuts import render
from django.http import Http404

#from .models import Pet
#from .models import Vaccine
from .models import *

def home(request):
    pets = Pet.objects.all()    # SELECT * FROM pet
    return render(request, 'home.html', {   # Takes pets, opens home.html, and does something with it
        'pets': pets,
    })

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('pet not found')
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })

def all_vaccines (request):
    vaccines = Vaccine.objects.all()
    return render(request, 'vaccines.html', {
        'vaccine_data': vaccines,   # Name in '' MUST match the variable called in the for loop in vaccines.html
    })