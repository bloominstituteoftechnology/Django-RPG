How many total Characters are there?
 302
 Character.objects.all().count()

How many of each specific subclass?
 68
 Character.objects.filter(fighter__gt=0).count()

How many total Items?
174
Item.objects.count()

How many of the Items are weapons? How many are not?
37
Weapon.objects.count()
137
Item.objects.filter(weapon__isnull=True).count()

On average, how many Items does each Character have?
'count__avg': 2.9735099337748343
averageItem = Character.objects.annotate(count=Count("inventory")).aggregate(Avg("count"))

On average, how many Weapons does each character have?
0.6721854304635762
averageWeapon = Character.objects.annotate(count=Count("inventory__weapon")).aggregate(Avg("count"))