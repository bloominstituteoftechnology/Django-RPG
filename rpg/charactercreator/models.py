from django.db import models

class Character(models.Model):
    """Abstract base representation of RPG characters."""
    name = models.CharField(max_length=30)
    level = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    hp = models.IntegerField(default=10)
    strength = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    wisdom = models.IntegerField(default=1)
    
    class Meta:
        abstract = True

class Fighter(Character):
    """Martial warrior class good at hitting things."""
    using_shield = models.BooleanField(default=False)
    rage = models.IntegerField(default=100)

class Mage(Character):
    """Arcane spellcasters with a familiar pet."""
    familiar_alive = models.BooleanField(default=True)
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
    familiar_alive = models.BooleanField(default=False)

# Multiple Inheritance
class Assassin(Fighter, Thief):
    # NOTE - game logic should probably forbid using_shield
    rage = models.IntegerField(default=50)
    energy = models.IntegerField(default=50)

class Paladin(Fighter, Cleric):
    rage = models.Integer(default=50)
    mana = models.Integer(default=50)
