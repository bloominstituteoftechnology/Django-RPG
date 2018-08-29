from charactercreator.models import Character, Thief, Fighter, Mage, Necromancer, Cleric
from django.db.models import Avg, Count

from armory.models import Item, Weapon

def count_char():
    c = Character.objects.all()
    count = c.count()
    return count

def count_thief():
    t = Thief.objects.all()
    count = t.count()
    return count

def count_mage():
    m = Mage.objects.all()
    count = m.count()
    return count

def count_cleric():
    cl = Cleric.objects.all()
    count = cl.count()
    return count

def count_necro():
    n = Necromancer.objects.all()
    count = n.count()
    return count

def count_fighter():
    f = Fighter.objects.all()
    count = f.count()
    return count

def count_items():
    i = Item.objects.all()
    icount = i.count()
    return icount

def count_weapons():
    w = Weapon.objects.all()
    wcount = w.count()
    return wcount

def not_weapons():
    not_weapon = count_items() - count_weapons()
    return not_weapon

def average_item():
    averageItem = Character.objects.annotate(count=Count("inventory")).aggregate(Avg("count"))
    return averageItem