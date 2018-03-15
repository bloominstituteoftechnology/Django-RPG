from django.db import models
from rpg.armory.models import Items

# Create your models of RPG characters here.
# do not push this and make and request as it will result in git conflicets 
class Character(models.Model):
    character_id = models.AutoField(primary_key=True)
    name = models.CharField("Character's name", max_length=30)
    level = models.IntegerField(default=0)
    hp = models.IntegerField(default=10)
    strength = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    inventory = models.ManyToManyField(Items, verbose_name="Items the character has")

""" For those close up encounters """
class Fighter(Character):
    using_shields = models.BooleanField(default=False)
    rage = models.IntegerField(default=100)

""" Adds the fuel to your fire """
class Mage(Character):
    mana = models.IntegerField(default=100)

""" Gives life to those in need """
class Cleric(Character):
    using_shields = models.BooleanField(default=False)
    mana = models.IntegerField(default=100)

""" When darkness becomes an ally """
class Thief(Character):
    is_sneaking = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=True)
    energy = models.IntegerField(default=100)

""" The Dead shall know the Living """
class Necromancer(Mage):
    talisman_charged = models.BooleanField(default=True)
    has_pet = models.BooleanField(default=False)

""" Death comes with silence """
class Assassin(Thief):
    rage = models.IntegerField(default=100)

""" Wisdom comes with time and experience """
class GrandWizard(Mage):
    staff_charged = models.BooleanField(default=True)
