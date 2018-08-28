In pipenv shell run
./manage.py shell


# How many total Characters are there?

>>> from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
>>> c = Character.objects.all()
>>> len(c)
302


# How many of each specific subclass?

>>> f = Fighter.objects.all()
>>> len(f)
68

>>> m = Mage.objects.all()
>>> len(m)
108

>>> cl = Cleric.objects.all()
>>> len(cl)
75

>>> t = Thief.objects.all()
>>> len(t)
51

>>> n = Necromancer.objects.all()
>>> len(n)
11


# How many total Items?

>>> from armory.models import Item, Weapon
>>> i = Item.objects.all()
>>> len(i)
174


# How many of the Items are weapons? How many are not?
>>> from armory.models import Item, Weapon
>>> i = Item.objects.all()
>>> len(i)
174
>>> 
>>> w = Weapon.objects.all()
>>> len(w)
37
>>> 
>>> len(i) - len(w)
137
>>> 