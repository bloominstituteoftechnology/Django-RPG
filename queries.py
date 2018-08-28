from charactercreator.models import Character
from armory.models import Item

Character.objects.count()  # 302 characters
Character.objects.filter(fighter__gt=0).count()  # 68
# mega 108
# clerk 75
# thief 51


Item.objects.count()  # 174

Item.objects.filter(weapon__gt=0).count()  # 37

Item.objects.count() / Character.objects.count()  # 0.5761589403973509

Item.objects.filter(weapon__gt=0).count() / Character.objects.count()  # 0.12251655629139073
