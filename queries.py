from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon 
from django.db.models import Count, Avg

# 1. How many total Characters are there? 

Character.objects.count() # There are 302 Characters. 

# 2. How many of each specific subclass?

Fighter.objects.count() # There are 68 Fighters.
Mage.objects.count() # There are 108 Mages.
Cleric.objects.count() # There are 75 Clerics. 
Thief.objects.count() # There are 51 Thieves. 

# 3. How many total Items?

Item.objects.count() # There are 174 Items. 

# 4. How many of the Items are weapons? How many are not?

Weapon.objects.count() # There are 37 Weapons. 
Item.objects.filter(weapon__isnull=True).count() # There 137 Items that are not Weapons. 

# 5. On average, how many Items does each Character have?

Character.objects.annotate(count=Count('inventory')).aggregate(Avg('count')) # The average number of Items each Character has is 2.9735099337748343. 

# 6. On average, how many Weapons does each character have?

Character.objects.annotate(count=Count('inventory__weapon')).aggregate(Avg('count')) # The average number of Weapons each Character has is 0.6721854304635762. 
