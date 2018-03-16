from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Character, Fighter, Mage, Cleric, Thief

def index(request):
    return HttpResponse("Character Creator App!")

<<<<<<< HEAD
@login_required
=======
>>>>>>> 6137dda1a64e090fa9968f967f5cc68132ff0c66
def view_all_characters(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters/index.html', context)

def view_character(request):
    # TODO
    pass
