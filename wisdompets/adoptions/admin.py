from django.contrib import admin

#from .models import Pet
#from .models import Vaccine
from .models import *

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ['name']