# Querying items with the Django ORM
from django.db.models import Count, Avg, Q
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
"""
num_fighters = Fighter.objects.count()
num_mages = Mage.objects.count()
num_clerics = Cleric.objects.count()
num_thieves = Thief.objects.count()
num_necromancers = Necromancer.objects.count()


"""
How many total items?
"""
num_items = Item.objects.count()


"""
How many of the items are weapons? How many are not?

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


"""
On average, how many items does each character have?

annotate() aggregates data for each object in a QuerySet
https://docs.djangoproject.com/en/2.1/ref/models/querysets/#annotate
https://docs.djangoproject.com/en/2.1/topics/db/aggregation/#s-generating-aggregates-for-each-item-in-a-queryset

aggregate() generates a summaries of values over the entire QuerySet
https://docs.djangoproject.com/en/2.1/ref/models/querysets/#aggregate
https://docs.djangoproject.com/en/2.1/topics/db/aggregation/#generating-aggregates-over-a-queryset

Aggregate functions: Avg, Count, Min, Max, Sum
https://docs.djangoproject.com/en/2.1/ref/models/querysets/#aggregation-functions
"""
avg_items_per_character = (
    Character.objects
    .annotate(
        items=Count('inventory'))
    .aggregate(
        Avg('items'))
)


"""
On average, how many weapons does each character have?

Aggregate functions have a filter argument
https://docs.djangoproject.com/en/2.1/topics/db/aggregation/#filtering-on-annotations
"""
avg_weapons_per_character = (
    Character.objects
    .annotate(
        weapons=Count('inventory', filter=Q(inventory__weapon__isnull=False)))
    .aggregate(
        Avg('weapons'))
)
