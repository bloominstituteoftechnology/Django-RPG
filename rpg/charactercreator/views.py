from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Character, Fighter, Mage, Cleric, Thief

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
    return render(request, 'character/index.html', {'character': character, 'charClass': charClass})

# context = {'character': character, 'charClass': charClass}
# return render(request, 'character/index.html', context)
