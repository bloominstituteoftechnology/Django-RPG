# How many total characters are there?

from charactercreator.models import Character, Thief, Fighter, Mage, Cleric, Necromancer
from armory.models import Item, Weapon
from django.db.models import Count, Avg

totalCharacters = Character.objects.count()  # 302

# How many of each specific subclass?

# Number of thieves:
numThieves = Thief.objects.count()  # 51

# Number of fighters:
numFighters = Fighter.objects.count()  # 68

# Number of mages:
numMages = Mage.objects.count()  # 108

# Number of clerics:
numClerics = Cleric.objects.count()  # 75

# Number of necromancers:
numNecromancers = Necromancer.objects.count()  # 11
# Though Necromancers are tricky because they're a subtype of Mage
# so they get counted twice, effectively

# How many total items?
numItems = Item.objects.count()  # 174

# How many of the items are weapons?
numWeapons = Weapon.objects.count()  # 37

# How many of the items are not weapons?
notWeapons = numItems - numWeapons  # 137

# What's the average number of items per character?
averageItem = Character.objects.annotate(count=Count("inventory")).aggregate(
    Avg("count")
)  # 2.97

# What's the average number of weapons each character has?
averageWeapon = Character.objects.annotate(count=Count("inventory__weapon")).aggregate(
    Avg("count")
)  # 0.67
