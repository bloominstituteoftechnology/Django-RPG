from django.db import models

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    value = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

class Weapon(Item):
    power = models.IntegerField(default=0)

class Potion(Item):
    hp_potion = models.IntegerField(default=10)
    strength_potion = models.IntegerField(default=10)