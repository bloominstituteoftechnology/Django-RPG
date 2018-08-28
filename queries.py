import sys
import os
import django
sys.path.append("./rpg")  # here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rpg.settings")
django.setup()


from charactercreator.models import *
from armory.models import *


if __name__ == "__main__":
    def total_items_by_type_of_character(character_type):
        """Calculates the summatory of items in this type of character"""
        total_items = 0
        for f in character_type:
            total_items += f.inventory.count()

        print(f'{total_items}')
        return total_items

    # How many total Characters are there?
    print("How many total Characters are there?\n*******************")
    characters = Character.objects.all()
    print(f'Total number of characters = {len(characters)}')  # 302

    # How many of each specific subclass?
    print("How many of each specific subclass?\n*******************")

    fighters = Fighter.objects.all()
    print(f'Total number of fighters = {len(fighters)}')  # 68

    mages = Mage.objects.all()
    print(f'Total number of mages = {len(mages)}')  # 108

    clerics = Cleric.objects.all()
    print(f'Total number of clerics = {len(clerics)}')  # 75

    thiefs = Thief.objects.all()
    print(f'Total number of thiefs = {len(thiefs)}')  # 51

    necromancers = Necromancer.objects.all()
    print(f'Total number of necromancers = {len(necromancers)}')  # 11

    # How many total Items?
    print("How many total Items?\n*******************")
    items = Item.objects.all()
    print(f'Total number of items = {len(items)}')  # 174

    # How many of the Items are weapons? How many are not?
    print("How many of the Items are weapons? How many are not?\n*******************")
    weapons = Weapon.objects.all()
    print(f'Total number of weapons = {len(weapons)}')  # 37
    print(f'Total number of NO-weapons = {len(items) - len(weapons)}')  # 137

    # On average, how many Items does each Character have?
    print("On average, how many Items does each Character have?\n*******************")

    characters_total_items = total_items_by_type_of_character(
        characters)  # 888
    print(
        f'Average items per Character = {characters_total_items / len(characters)}')  # 2.97

    # On average, how many Weapons does each character have?
    print("On average, how many Weapons does each character have?\n*******************")

    fighters_total_items = total_items_by_type_of_character(fighters)  # 214
    print(
        f'Average items per Fighter = {fighters_total_items / len(fighters)}')  # 3.147

    mages_total_items = total_items_by_type_of_character(mages)  # 331
    print(
        f'Average items per Mages = {mages_total_items / len(mages)}')  # 3.064

    clerics_total_items = total_items_by_type_of_character(clerics)  # 193
    print(
        f'Average items per Clerics = {clerics_total_items / len(clerics)}')  # 2.573

    thiefs_total_items = total_items_by_type_of_character(thiefs)  # 160
    print(
        f'Average items per Thiefs = {thiefs_total_items / len(thiefs)}')  # 3.137

    necromancers_total_items = total_items_by_type_of_character(
        necromancers)  # 31
    print(
        f'Average items per Necromancers = {necromancers_total_items / len(necromancers)}')  # 2.818
