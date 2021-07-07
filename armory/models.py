from django.db import models

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    value = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Weapon(Item):
    power = models.IntegerField(default=0)
