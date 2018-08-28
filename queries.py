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

>>> len(items) / len(c)
0.5761589403973509 #average number of items per character

>>> len(weapons) / len(c)
0.12251655629139073 #average number of weapons per character