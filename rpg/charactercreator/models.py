from django.db import models
from rpg.armory.models import Item

# create the character class and establish the fields to associate with characters
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
    # inventory is a many to many field which extends to Item
    inventory = models.ManyToManyField(Item, verbose_name="Items the character has")

# the following are classes that extend Character
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

# Necros extend Mage, which extends Character
class Necromancer(Mage):
    """Spellcaster specialized in the arts of the undead."""
    # Charged talismans can be used to raise the dead!
    talisman_charged = models.BooleanField(default=True)
