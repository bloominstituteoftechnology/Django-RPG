''' How many total Characters are there? '''
from charactercreator.models import Character
characters = Character.objects.all()
len(characters) 

''' How many of each specific subclass? '''
from charactercreator.models import Fighter, Mage, Cleric, Thief, Necromancer
fighters = Fighter.objects.count()
mages = Mage.objects.count() - Necromancer.objects.count
clerics = Cleric.objects.count()
thieves = Thief.objects.count()
necromancers = Necromancer.objects.count()

''' How many total Items? '''
from armory.models import Item, Weapon
items = Item.objects.count()

''' How many of the Items are weapons? How many are not? '''
weapons = Weapon.objects.count()
non-weapons = items - weapons

''' On average, how many Items does each Character have? '''
from django.db.models import Count, Avg
c = Character.objects.all().annotate(count=Count('inventory'))
c.aggregate(Avg('count'))

''' On average, how many Weapons does each character have? '''
Character.objects.annotate(items=Count('inventory__weapon')).aggregate(Avg('items')) '''double underscores( __ ) are used for Field Lookups'''



