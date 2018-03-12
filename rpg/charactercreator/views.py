from django.http import HttpResponse
from django.shortcuts import render
from .models import Character, Fighter, Mage, Cleric, Thief, Necromancer

def getType(character):
    if Fighter.objects.filter(pk=character.character_id).exists():
        return {"name": 'fighter', "fields": [{"t": 'Using Shield', "v":  character.fighter.using_shield}, {"t": 'Rage',  "v": character.fighter.rage}]  }
    if Mage.objects.filter(pk=character.character_id).exists():
        return {"name": 'Mage', "fields": [{"t": 'Has Pet', "v":  character.mage.has_pet}, {"t": 'Mana',  "v": character.mage.mana}]  }
    if Cleric.objects.filter(pk=character.character_id).exists():
        return {"name": 'Cleric', "fields": [{"t": 'Using Shield', "v":  character.cleric.using_shield}, {"t": 'Mana',  "v": character.cleric.mana}]  }
    if Thief.objects.filter(pk=character.character_id).exists():
        return {"name": 'Thief',  "fields": [{"t": 'Is Sneaking', "v":  character.thief.is_sneaking}, {"t": 'Energy',  "v": character.thief.energy}]  }
    if Necromancer.objects.filter(pk=character.character_id).exists():
        return {"name": 'Necromancer', "fields": [ {"t": 'Talisman Charged', "v":  character.necromancer.talisman_charged}]  }

def index(request):
    return view_all_characters(request)  # HttpResponse("Character Creator Appal!")

def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'charactercreator/index.html', context)

def view_character(request,character_id):
    character = Character.objects.get(pk=character_id)
    ct = getType(character)
    context = {'character': character, 'ct': ct}
    return render(request, 'charactercreator/character.html', context)
