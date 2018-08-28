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