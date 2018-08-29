from django.contrib import admin
from .models import Item
from .models import Weapon

# Register your models here.
admin.site.register(Item)
admin.site.register(Weapon)
