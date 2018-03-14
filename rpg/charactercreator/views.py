<<<<<<< HEAD
#from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

=======
from django.contrib.auth.decorators import login_required
>>>>>>> 13039317107759a9dd72e257da95f513b433f6fd
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

def view_character(request):
    # TODO
    pass
