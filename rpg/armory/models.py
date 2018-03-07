from django.db import models

# Create your models here.

class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30)
    value = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

class Weapon(Items):
    power = models.IntegerField(default=0)
    