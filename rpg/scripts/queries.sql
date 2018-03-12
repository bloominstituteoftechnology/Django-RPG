

select COUNT(*) as "total Character"  from charactercreator_character;
select COUNT(*) as "total Fighters"  from charactercreator_fighter;
select COUNT(*) as "total Mages"  from charactercreator_mage;
select COUNT(*) as "total Clerics"  from charactercreator_cleric;
select COUNT(*) as "total Thiefs"  from charactercreator_thief;
select COUNT(*) as "total Necromancer"  from charactercreator_Necromancer;


-- SELECT COUNT(*) AS "unique items_count" FROM "armory_item";
-- SELECT COUNT(*) AS "unique weapons_count" FROM "armory_weapon";
select COUNT(*) as "total Items" from  (select *  from charactercreator_character_inventory group by character_id, item_id);
-- [select Count(*) 'total Items:'  from charactercreator_character_inventory;] also works, there are no (character_id, item_id) dups in test data

select COUNT(*) as 'total Weapons' from charactercreator_character_inventory JOIN armory_weapon on charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id; 

select COUNT(*) as "total Items that are not Weapons" from  (select *  from charactercreator_character_inventory where item_id not in (select item_ptr_id from armory_weapon));

SELECT AVG("count") as "average number of Items per Character" FROM (SELECT COUNT("charactercreator_character_inventory"."item_id") AS "count" FROM "charactercreator_character" LEFT JOIN "charactercreator_character_inventory" ON ("charactercreator_character"."character_id" = "charactercreator_character_inventory"."character_id") GROUP BY "charactercreator_character"."character_id");


SELECT AVG("count") as "average number of Weapons per Character" FROM (SELECT COUNT("armory_weapon"."item_ptr_id") AS "count" FROM "charactercreator_character" LEFT JOIN "charactercreator_character_inventory" ON ("charactercreator_character"."character_id" = "charactercreator_character_inventory"."character_id")  LEFT JOIN armory_weapon on charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
       GROUP BY "charactercreator_character"."character_id");
