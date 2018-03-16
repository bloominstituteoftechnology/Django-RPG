from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Character, Fighter, Mage, Cleric, Thief, Necromancer, Walker, Runner, Berzerker
from django import template

# everything that follows @login_required will hide the endpoint until a user logs in


def index(request):
    return render(request, 'main/index.html')