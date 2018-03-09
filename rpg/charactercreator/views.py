from django.http import HttpResponse
from django.shortcuts import render
from .models import Character, Fighter, Mage, Cleric, Thief


def index(request):
    return HttpResponse("Character Creator App!")


def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters/index.html', context)


def view_character(request, character_id):
    character = Character.objects.get(pk=character_id)
    context = {'character': character}
    return render(request, 'character/index.html', context)
