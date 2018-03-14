from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Character, Fighter, Mage, Cleric, Thief
from armory.models import Item


@login_required
def index(request):
    context = {

    }
    return render(request, 'charactercreator/index.html', context)


@login_required
def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters/index.html', context)


def view_character(request, character_id):
    character = Character.objects.get(pk=character_id)
    context = {'character': character}
    return render(request, 'character/index.html', context)
