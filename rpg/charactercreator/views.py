from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Character, Fighter, Mage, Cleric, Thief, Necromancer, Beast, Zombie
from django import template

register = template.Library()


def index(request):
    return HttpResponse("Character Creator App!")


@login_required
def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters/index.html', context)


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
                        charClass = character.beast.__class__.__name__
                    except:
                        try:
                            charClass = character.zombie.__class__.__name__
                        except:
                            pass
    return render(request, 'characters/detail.html', {'character': character, 'charClass': charClass})


@register.filter
def to_class_name(value):
    return value.__class__.__name__
