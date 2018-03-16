from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Character, Fighter, Mage, Cleric, Thief
from django import template

# everything that follows @login_required will hide the endpoint until a user logs in


def index(request):
    return HttpResponse("Character Creator App!")


@login_required
def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters/index.html', context)


@login_required
def view_character(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
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
                    try:
                        charClass = character.necromancer.__class__.__name__
                    except:
                        try:
                            charClass = character.walker.__class__.__name__
                        except:
                            try:
                                charClass = character.runner.__class__.__name__
                            except:
                                try:
                                    charClass = character.berzerker.__class__.__name__
                                except:
                                    pass
    return render(request, 'character/index.html', {'character': character, 'charClass': charClass})

# context = {'character': character, 'charClass': charClass}
# return render(request, 'character/index.html', context)
