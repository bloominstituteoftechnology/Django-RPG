from django.db import models
from armory.models import Item


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
    inventory = models.ManyToManyField(
    Item, verbose_name="Items the character has")


class Fighter(Character):
    """Martial warrior class good at hitting things."""
    # using_shield = models.BooleanField(default=False)
    # rage = models.IntegerField(default=100)

    def class_name(self):
        return self.__class__.__name__


class Mage(Character):
    """Arcane spellcasters with a familiar pet."""
    # has_pet = models.BooleanField(default=True)
    # mana = models.IntegerField(default=100)

    def class_name(self):
        return self.__class__.__name__


class Cleric(Character):
    """Mystical healers who can use shields."""
    # using_shield = models.BooleanField(default=False)
    # mana = models.IntegerField(default=100)

    def class_name(self):
        return self.__class__.__name__


class Thief(Character):
    """Sneaky rogues good at stealth and ranged attacks."""
    # is_sneaking = models.BooleanField(default=False)
    # energy = models.IntegerField(default=100)

    def class_name(self):
        return self.__class__.__name__


class Necromancer(Mage):
    """Spellcaster specialized in the arts of the undead."""
    # Charged talismans can be used to raise the dead!
    # talisman_charged = models.BooleanField(default=True)

    def class_name(self):
        return self.__class__.__name__


class Beast(Character):
    """A wild beast that contains a vast amount of rage and strength"""
    # rage = models.IntegerField(default=300)
    # strength = models.IntegerField(default=5)
    # mana = Nonepython manage.py shell
    # energy = None

    def class_name(self):
        return self.__class__.__name__


class Zombie(Character):
    """A creature of the dead that has the ability to take extra damage"""
    # mana = None
    # energy = None
    # rage = models.IntegerField(default=100)
    # hp = models.IntegerField(default=50)

    def class_name(self):
        return self.__class__.__name__
