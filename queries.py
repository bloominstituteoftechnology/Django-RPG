# get all characters
from charactercreator.models import Character

all_characters = Character.objects.all()
print(len(all_characters)) # 302

