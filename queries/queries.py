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
numCharacters = Character.objects.count()
