from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Character, Fighter, Mage, Cleric, Thief


def index(request):
    return HttpResponse("Character Creator App!")


@login_required
def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters/index.html', context)


def view_character(request, character_id):
    character = Character.objects.get(pk=character_id)
    try:
        charClass = character.fighter.__class__.__name__
    except:
        try:
            charClass = character.mage.__class__.__name__
        except:
            try:
                charClass = character.thief.__class__.__name__
            except:
                try:
                    charClass = character.cleric.__class__.__name__
                except:
                    pass
    context = {'character': character, 'charClass': charClass}
    return render(request, 'character/index.html', context)
