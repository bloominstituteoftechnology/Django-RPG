
def run():
    from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
    from armory.models import Item, Weapon
    from decimal import Decimal
    items_count = Item.objects.count()
    weapons_count = Weapon.objects.count()
    character_count = Character.objects.count()
    print('total Characters: {0}'.format(character_count))
    print('total Fighters: {0}'.format(Fighter.objects.count()))
    print('total Mages: {0}'.format(Mage.objects.count()))
    print('total Clerics: {0}'.format(Cleric.objects.count()))
    print('total Thiefs: {0}'.format(Thief.objects.count()))
    print('total Necromancers: {0}'.format(Necromancer.objects.count()))
    icount = 0
    wcount = 0
    for c in Character.objects.all():
        icount += c.inventory.count()
        wcount += c.inventory.exclude(weapon=None).count()    
    print('total Items: {0}'.format(icount))
    print('total Weapons: {0}'.format(wcount))
    print('total Items not Weapons: {0}'.format(icount - wcount))   

    print('average number of Items per Character {0}'.format(icount/character_count))
    print('average number of Weapons per Character {0}'.format(wcount/character_count))

"""
total Characters: 302
total Fighters: 68
total Mages: 108
total Clerics: 75
total Thiefs: 51
total Necromancers: 11
total Items: 898
total Weapons: 203
total Items not Weapons: 695
average number of Items per Character 2.9735099337748343
average number of Weapons per Character 0.6721854304635762

total Character = 302
total Fighters = 68
total Mages = 108
total Clerics = 75
total Thiefs = 51
total Necromancer = 11
total Items = 898
total Weapons = 203
total Items that are not Weapons = 695
average number of Items per Character = 2.97350993377483
average number of Weapons per Character = 0.672185430463576




"""

