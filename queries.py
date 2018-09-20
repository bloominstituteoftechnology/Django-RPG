# import all character models
from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer

# get all characters
all_characters = Character.objects.all()
print(len(all_characters)) # 302

# get all fighters
all_fighters = Fighter.objects.all()
print(len(all_fighters)) # 68

# get all mages
all_mages = Mage.objects.all()
print(len(all_mages)) #108

# get all Clerics
all_clerics = Cleric.objects.all()
print(len(all_clerics)) #75

# get all Thieves
all_thieves = Thief.objects.all()
print(len(all_thieves)) #51

# get all Necromancers
all_necromancers = Necromancer.objects.all()
print(len(all_necromancers)) # 11