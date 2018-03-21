from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Item, Weapons

def index(request):
    return HttpResponse("Armory App!")

@login_required
def view_all_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'items/index.html', context)

def view_item(request):
    # TODO
    pass