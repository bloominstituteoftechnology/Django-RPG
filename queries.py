Total number of Characters
count = Character.objects.filter().count()
print(count)
302

Fighters
fight = Fighter.objects.filter().count()
68

# I used the same query for all of these
Mage
108

Cleric
75

Thief
51

Necromancer
11

Total Items
174

Weapons
37

Other - subtract Weapons from Total
137

-----
Average number of items
from django.db.models import Avg

c = Character.objects.all().aggregate(Avg('inventory'))
{inventory_avg": 89.17817371937639}

