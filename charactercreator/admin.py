from django.contrib import admin
from .models import Character
from .models import Fighter
from .models import Mage
from .models import Cleric
from .models import Thief
from .models import Necromancer
# Register your models here.
admin.site.register(Character)
admin.site.register(Fighter)
admin.site.register(Mage)
admin.site.register(Cleric)
admin.site.register(Thief)
admin.site.register(Necromancer)
