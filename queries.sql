.tables

.headers on
.mode column

/* How many characters are there? = 302*/
SELECT COUNT(character_id) from charactercreator_character;

/* How many of each subclass? */

/* How many thieves are there? = 51*/
SELECT COUNT(character_ptr_id) from charactercreator_thief;

/* How many fighters are there? = 68 */
SELECT COUNT(character_ptr_id) from charactercreator_fighter;

/* How many mages are there? = 108 */
SELECT COUNT(character_ptr_id) from charactercreator_mage;

/* How many clerics are there? = 75 */
SELECT COUNT(character_ptr_id) from charactercreator_cleric;

/* How many necromancers are there? = 11 */
SELECT COUNT(mage_ptr_id) from charactercreator_necromancer;

/* How many total items? = 174 */
SELECT COUNT(item_id) from armory_item;

/* How many of the items are weapons? = 37 */
SELECT COUNT(*), armory_item.name, armory_item.value, armory_item.weight, armory_item.item_id, armory_weapon.power FROM armory_item INNER JOIN armory_weapon ON armory_item.item_id=armory_weapon.item_ptr_id;
