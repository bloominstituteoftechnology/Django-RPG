from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Character, Fighter, Mage, Cleric, Thief

def getType(character):
    if Fighter.objects.filter(pk=character.character_id).exists():
        return{"type": 'Fighter'}
    if Mage.objects.filter(pk=character.character_id).exists():
        return{"type": 'Mage'}
    if Cleric.objects.filter(pk=character.character_id).exists():
        return{"type": 'Cleric'}
    if Thief.objects.filter(pk=character.character_id).exists():
        return{"type": 'Theif'}

def index(request):
    return HttpResponse("Character Creator App!")

@login_required
def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters/index.html', context)

def view_character(request):
    character = Character.objects.get(character_id)
    charType = getType(character)
    context = {'character': character, 'charType': charType}
    return render(request, 'character/index.html', context)