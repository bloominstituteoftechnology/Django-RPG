from django.contrib import admin
from .models import Character, Fighter, Mage, Cleric, Thief, Necromancer

admin.site.register((Character, Fighter, Mage, Cleric, Thief, Necromancer))
