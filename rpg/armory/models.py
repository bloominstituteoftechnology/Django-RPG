from django.db import models

# create class Item and create base fields for all items
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    value = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

# create weapon class which extends Items
class Weapon(Item):
    power = models.IntegerField(default=0)
