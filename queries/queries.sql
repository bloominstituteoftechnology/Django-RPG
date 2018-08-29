-- Querying items with the raw SQL commands

-- How many total Characters are there?
SELECT COUNT(character_id) FROM charactercreator_character;

-- How many of each specific subclass?
SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;
SELECT COUNT(character_ptr_id) FROM charactercreator_mage;
SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;
SELECT COUNT(character_ptr_id) FROM charactercreator_thief;
SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;