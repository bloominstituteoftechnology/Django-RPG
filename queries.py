import sqlite3

db = sqlite3.connect('./mydatabase')

cur = db.cursor()

# How many total characters
total_characters = cur.execute('SELECT count(*) from charactercreator_character')
total_characters_value = total_characters.fetchone()
print(total_characters_value[0])
#answer 302
# How many total clerics
cur.execute('SELECT count(*) from charactercreator_cleric')
print(cur.fetchall())
#answer 75
# How many total thiefs
cur.execute('SELECT count(*) from charactercreator_thief')
print(cur.fetchall())
#answer 51
# How many total fighters
cur.execute('SELECT count(*) from charactercreator_fighter')
print(cur.fetchall())
#answer 68
# How many total mages
cur.execute('SELECT count(*) from charactercreator_mage')
print(cur.fetchall())
#answer 108
# How many total necromancers
necro_data = cur.execute('SELECT count(*) from charactercreator_necromancer')
necro_value = necro_data.fetchone()
print(necro_value[0])
#answer 11
# How many total Items
total_items = cur.execute('SELECT count(*) from armory_item')
total_items_value = total_items.fetchone()
print(total_items_value[0])
#answer 174
# How many of the items are weapons
total_weapons = cur.execute('select count(*) from armory_weapon')
total_weapons_value = total_weapons.fetchone()
print(total_weapons_value[0])
#answer 37
# How many of the items are not weapons
items_total = (total_items_value[0] - total_weapons_value[0])
print(items_total)
#answer 137
# on average how many items does each character have?
total_inv = cur.execute('select count(*) from charactercreator_character_inventory')
total_inv_value = total_inv.fetchone()
average_num_items = (total_inv_value[0] / total_characters_value[0])
print(average_num_items)
#answer 2.973...
# On average, how many weapons does each character have?
weap_in_inv = cur.execute('select count(item_id) from charactercreator_character_inventory where item_id between 138 and 174')
total_weap_in_inv = weap_in_inv.fetchone()
average_weap_per_char = (total_weap_in_inv[0] / total_characters_value[0])
print(average_weap_per_char)
#answer 0.67
db.close()

# * [ ] How many total Characters are there?
# select count(*) from charactercreator_character;
# * [ ] How many of each specific subclass?
# * [ ] How many total Items?
# * [ ] How many of the Items are weapons? How many are not?
# * [ ] On average, how many Items does each Character have?
# * [ ] On average, how many Weapons does each character have?


