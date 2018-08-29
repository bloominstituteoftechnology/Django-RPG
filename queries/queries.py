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


"""
How many of the items are weapons? How many are not?

count() returns the number of objects matching the QuerySet
https://docs.djangoproject.com/en/2.1/ref/models/querysets/#count

filter() returns a new set that matches the given paramters
https://docs.djangoproject.com/en/2.1/ref/models/querysets/#filter

Field lookups can be used as a paramter in filter() (and exclude() and get())
Field lookups correspond to the sql WHERE command
https://docs.djangoproject.com/en/2.1/ref/models/querysets/#field-lookups

The field lookup isnull checks if a field is or is not set to null:
SELECT ... WHERE field IS NULL (or IS NOT NULL)
https://docs.djangoproject.com/en/2.1/ref/models/querysets/#std:fieldlookup-isnull
"""
num_weapons = Weapon.objects.count()
num_items_not_weapons = Item.objects.filter(weapon__isnull=True).count()
