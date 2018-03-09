from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Character, Fighter, Mage, Cleric, Thief, Necromancer, Beast, Zombie

def index(request):
    return HttpResponse("Character Creator App!")

def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters/index.html', context)

def view_character(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'characters/detail.html', {'character': character})
