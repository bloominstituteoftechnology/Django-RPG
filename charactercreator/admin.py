from django.contrib import admin
from .models import Character, Fighter, Mage, Thief, Cleric, Necromancer
# Register your models here.
admin.site.register(Character)
admin.site.register(Fighter)
admin.site.register(Mage)
admin.site.register(Thief)
admin.site.register(Cleric)
admin.site.register(Necromancer)