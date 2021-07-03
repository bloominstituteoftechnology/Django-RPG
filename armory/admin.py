from django.contrib import admin
from .models import Item, Weapon

admin.site.register((Item, Weapon))
