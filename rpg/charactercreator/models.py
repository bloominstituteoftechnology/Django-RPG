from django.db import models
from armory.models import Items

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
    mana = models.IntegerField(default=0)
    energy = models.IntegerField(default=0)
    has_pet = models.BooleanField(default=False)
    inventory = models.ManyToManyField(Items, verbose_name="Items the character has")
    class Meta: 
        # you can no longer instantiate character, no schema or table will exist for Character
        abstract = True
""" For those close up encounters """
class Fighter(Character):
    using_shields = models.BooleanField(default=False)
    rage = models.IntegerField(default=100)
    mana = None
    energy = None

""" Adds the fuel to your fire """
class Mage(Character):
    pet_alive = models.BooleanField(default=True)
    mana = models.IntegerField(default=100)
    energy = None
    rage = None
""" Gives life to those in need """
class Cleric(Character):
    using_shields = models.BooleanField(default=False)
    mana = models.IntegerField(default=100)
    rage = None
    energy = None
""" When darkness becomes an ally """
class Thief(Character):
    is_sneaking = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=True)
    energy = models.IntegerField(default=100)
    mana = None
    rage = None
""" The Dead shall know the Living """
class Necromancer(Mage):
    talisman_charged = models.BooleanField(default=True)
    Mage.pet_alive = models.BooleanField(default=False)

""" Death comes with silence """
class Assassin(Thief):
    Fighter.rage = models.IntegerField(default=50)
    Thief.energy = models.IntegerField(default=50)

""" A Good sword protects a kingdom """
class Paladin(Fighter):
    Fighter.rage = models.IntegerField(default=50)

""" Wisdom comes with time and experience """

class GrandWizard(Mage):
    Mage.mana = models.IntegerField(default=200)
    staff_charged = models.BooleanField(default=True)
