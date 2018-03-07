from django.db import models

class Character(models.Model):
    """Abstract base representation of RPG characters."""
    character_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    level = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    hp = models.IntegerField(default=10)
    strength = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    wisdom = models.IntegerField(default=1)
    has_pet = models.BooleanField(default=False)
    rage = models.IntegerField(default=0)
    mana = models.IntegerField(default=0)
    energy = models.IntegerField(default=0)

    class Meta:
        abstract = True

class Fighter(Character):
    """Martial warrior class good at hitting things."""
    using_shield = models.BooleanField(default=False)
    rage = models.IntegerField(default=100)
    mana = None
    energy = None

class Mage(Character):
    """Arcane spellcasters with a familiar pet."""
    has_pet = models.BooleanField(default=True)
    rage = None
    mana = models.IntegerField(default=100)
    energy = None

class Cleric(Character):
    """Mystical healers who can use shields."""
    using_shield = models.BooleanField(default=False)
    rage = None
    mana = models.IntegerField(default=100)
    energy = None

class Thief(Character):
    """Sneaky rogues good at stealth and ranged attacks."""
    is_sneaking = models.BooleanField(default=False)
    rage = None
    mana = None
    energy = models.IntegerField(default=100)

class Necromancer(Mage):
    """Spellcaster specialized in the arts of the undead."""
    # Charged talismans can be used to raise the dead!
    # TODO - Game logic should balance by weakening pet
    talisman_charged = models.BooleanField(default=True)
