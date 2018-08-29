# Querying items with the Django ORM
from armory.models import Item, Weapon
from charactercreator.models import (
    Character,
    Fighter,
    Mage,
    Cleric,
    Thief,
    Necromancer
)


"""
How many total Characters are there?

count() returns the number of objects matching the QuerySet
https://docs.djangoproject.com/en/2.1/ref/models/querysets/#count
"""
num_characters = Character.objects.count()


"""
How many of each specific subclass?

count() returns the number of objects matching the QuerySet
https://docs.djangoproject.com/en/2.1/ref/models/querysets/#count
"""
num_fighters = Fighter.objects.count()
num_mages = Mage.objects.count()
num_clerics = Cleric.objects.count()
num_thieves = Thief.objects.count()
num_necromancers = Necromancer.objects.count()


"""
How many total items?

count() returns the number of objects matching the QuerySet
https://docs.djangoproject.com/en/2.1/ref/models/querysets/#count
"""
num_items = Item.objects.count()
