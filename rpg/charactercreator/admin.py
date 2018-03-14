from django.contrib import admin

# Register your models here.
from .models import Character, Fighter, Mage, Cleric, Thief
from armory.models import Item

admin.site.register(Character)
admin.site.register(Fighter)
admin.site.register(Mage)
admin.site.register(Cleric)
admin.site.register(Thief)
admin.site.register(Item)
