from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Character, Fighter, Mage, Cleric, Thief

def index(request):
    return HttpResponse("Character Creator App!")

@login_required
def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters/index.html', context)

@login_required
def view_character(request, character_id):
    try:
        character = Character.objects.get(pk=character_id)
        context = {'character': character}
        return render(request, 'characters/detail.html', context)
    except Character.DoesNotExist:
        raise Http404("No Character matches the given query.")

@login_required
def view_all_items(request, character_id):
    character = Character.objects.get(pk=character_id) 
    items = character.inventory.get_queryset()
    context = {'items': items}
    return render(request, 'characters/items.html', context)
