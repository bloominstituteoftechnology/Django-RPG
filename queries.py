# How many total Characters are there?
from charactercreator.models import *
from armory.models import *
chars = Character.objects.all()
# 302
len(chars)

# How many of each specific subclass?

sub_classes = {subclass.__name__.lower():[] for subclass in chars[0].__class__.__subclasses__()}

for char in chars:

    if hasattr(char, 'fighter'):
        sub_classes['fighter'].append(char)

    if hasattr(char, 'mage'):
        sub_classes['mage'].append(char)

    if hasattr(char, 'cleric'):
        sub_classes['cleric'].append(char)

    if hasattr(char, 'thief'):
        sub_classes['thief'].append(char)

# 68
fighters_len = len(sub_classes['fighter'])

# 108
mages_len = len(sub_classes['mage'])

# 75
clerics_len = len(sub_classes['cleric'])

# 51
thieves_len = len(sub_classes['thief'])

# 11
necromancers_len = len(Necromancer.objects.all())

#  How many of the Items are weapons? How many are not?

# 174
items = Item.objects.all()
len(items)

# 37
weapons = Weapon.objects.all()
len(weapons)


#  On average, how many Items does each Character have?
# 2.9735099337748343


inventories = [len(char.inventory.get_queryset()) for char in Character.objects.all()]

from functools import reduce
average_inventory = reduce((lambda num1, num2: num1 + num2), inventories) / len(inventories)

# On average, how many Weapons does each character have?
