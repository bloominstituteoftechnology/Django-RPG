from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Item, Weapon 

def index(request):
    return HttpResponse("Character Creator App at Armory view!")

def view_all_armory(request):
    items = Items.objects.all()
    context = {'items': items}
    return render(request, 'items/index.html', context)

def view_character(request):
    # TODO
    pass
# from django.http import HttpResponse
# from django.shortcuts import render
# from .models import Character, Fighter, Mage, Cleric, Thief

# def index(request):
#     return HttpResponse("Character Creator App!")

# def view_all_characters(request):
#     characters = Character.objects.all()
#     context = {'characters': characters}
#     return render(request, 'characters/index.html', context)

# def view_character(request):
#     # TODO
#     pass