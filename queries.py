>python ./manage.py shell
>>> from charactercreator.models import Character
>>> c = Character.objects.all()
>>> len(c)
302 #number of total Characters

>>> from charactercreator.models import Fighter
>>> fighters = Fighter.objects.all()
>>> len(fighters)
68 #number of Fighters
>>> from charactercreator.models import Mage, Cleric, Thief, Necromancer
>>> mages = Mage.objects.all()
>>> len(mages)
108 #number of mages
>>> clerics = Cleric.objects.all()
>>> len(clerics)
75 #number of Clerics
>>> thiefs = Thief.objects.all()
>>> len(thiefs)
51 #number of Thiefs
>>> necromancers = Necromancer.objects.all()
>>> len(necromancers)
11 #number of necromancers

>>> from armory.models import Item, Weapon
>>> items = Item.objects.all()
>>> len(items)
174 #total number of items

>>> weapons = Weapon.objects.all()
>>> len(weapons)
37 #total number of weapons
>>> len(items) - len(weapons)
137 #number of items that are not weapons

>>> from django.db.models import Avg, Count
>>> averageItemsPerCharacter = Character.objects.annotate(count=Count("inventory")).aggregate(Avg("count"))
>>> averageItemsPerCharacter
{'count__avg': 2.9735099337748343} #average number of items per character
>>> Character.objects.annotate(count=Count("inventory__weapon")).aggregate(Avg("count"))
{'count__avg': 0.6721854304635762} #average number of weapons per character