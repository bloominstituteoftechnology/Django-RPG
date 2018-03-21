from django.db import models
from rpg.armory.models import Item

<<<<<<< HEAD
# Create your models here.
class Character(models.Model):
	""" Abstract base representation of RPG characters. """
	name = models.CharField(max_length=30)
	level = models.IntegerField(default=0)
	exp = models.IntegerField(default=0)
	hp = models.IntegerField(default=10)
	strength = models.IntegerField(default=1)
	intelligence = models.IntegerField(default=1)
	dexterity = models.IntegerField(default=1)
	wisdom = models.IntegerField(default=1)
	#inventory = models.ManyToManyField(Item)

	class Meta:
		abstract = True

class Fighter(Character):
	""" Martial warrior class good at hitting things. """
	using_shield = models.BooleanField(default=False)
	rage = models.IntegerField(default=100)

class Mage(Character):
	""" Arcane spellcasters with a familiar pet. """
	familiar_alive = models.BooleanField(default=False)
	mana = models.IntegerField(default=100)

class Cleric(Character):
	""" Mystical healers who can use sheilds. """
	using_shield = models.BooleanField(default=False)
	mana = models.IntegerField(default=100)

class Thief(Character):
	""" Sneaky rouges good at stealth and ranged attacks. """
	is_sneaking = models.BooleanField(default=False)
	energy = models.IntegerField(default=100)

class Necromancer(Mage):
	""" Spellcaster specialized in the arts of the undead. """
	# Charged talismans can be used to raise the dead!
	talisman_charged = models.BooleanField(default=True)
	familiar_alive = models.BooleanField(default=False)

# Multiple Inheritance
class Assassin(Fighter, Theif):
	# Note: game logic should probably forbid using_shield
	rage = models.IntegerField(default=50)
	energy = models.IntegerField(default=50)

class Paladin(Fighter, Cleric):
	rage = models.IntegerField(default=50)
	mana = models.IntegerField(default=50)

#ToDO Inventory
#class Item(models.Model):
=======
class Character(models.Model):
    """Base representation of RPG characters."""
    character_id = models.AutoField(primary_key=True)
    name = models.CharField("Character's name", max_length=30)
    level = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    hp = models.IntegerField(default=10)
    strength = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    wisdom = models.IntegerField(default=1)
    inventory = models.ManyToManyField(Item, verbose_name="Items the character has")

class Fighter(Character):
    """Martial warrior class good at hitting things."""
    using_shield = models.BooleanField(default=False)
    rage = models.IntegerField(default=100)

class Mage(Character):
    """Arcane spellcasters with a familiar pet."""
    has_pet = models.BooleanField(default=True)
    mana = models.IntegerField(default=100)

class Cleric(Character):
    """Mystical healers who can use shields."""
    using_shield = models.BooleanField(default=False)
    mana = models.IntegerField(default=100)

class Thief(Character):
    """Sneaky rogues good at stealth and ranged attacks."""
    is_sneaking = models.BooleanField(default=False)
    energy = models.IntegerField(default=100)

class Necromancer(Mage):
    """Spellcaster specialized in the arts of the undead."""
    # Charged talismans can be used to raise the dead!
    talisman_charged = models.BooleanField(default=True)
>>>>>>> f69cff9ae835a080b9b5a151cdf919c751f92b11
