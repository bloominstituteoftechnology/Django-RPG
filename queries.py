import sqlite3

conn = sqlite3.connect('django.db.backends.sqlite3')
c = conn.cursor()
# sqlite_file = './mydatabase'

# * [ ] How many total Characters are there? 302
# select count(*) from charactercreator_character;
# * [ ] How many of each specific subclass?
# select count(*) from charactercreator_cleric;
#   cleric = 75
#   thief = 51
#   mage = 108;
#   figher = 68;
#   necromancer = 11;
# * [ ] How many total Items?
# 174
# * [ ] How many of the Items are weapons? How many are not?
#   weapons = 37;
#   other = 137;
# * [ ] On average, how many Items does each Character have?
#   2.92
# * [ ] On average, how many Weapons does each character have?



SELECT
count(*)
FROM
charactercreator_character;

SELECT
count(*)
FROM
charactercreator_cleric