Minimum Viable RPG
Story / flow
Our hero is going down the road.
Monsters emerge from the shadows.
Our hero must defeat the monster to continue!
Monsters continue emerging of increasing difficulty, with some randomness
Boss monsters every 10 levels
(Optional) After each boss, have an option to visit a shop (sell loot, maybe buy items), or a traveling merchant just happens to come down the road
Entities
Characters
Base classes - Fighter, Mage, Cleric, Thief
Extended classes - Necromancer (given), + student implemented
Player controls 1 character (multi-character is stretch goal)
Monsters
Base monster types - Goblin, Orc, Zombies, Ghouls, Unicorn, etc.
*Random* extended monsters
Some long list of adjectives (venomous, berserker, odiferous, giant, etc.), maybe also nouns
Randomly combine them + base monsters to generate unique-ish enemies
Randomly assign loot based on the level/power of monster
Boss subclass (with more abilities/power)
Loot (Items)
Some items (Weapons, Armor) are equippable, and increase attack/defense
Other items are not equippable, and are just loot to be sold/increase score
(Optional) upgrade equippable items (maybe paying gold to do so)
Actions
Fighting
Coin flip to randomize player / monster starting first
Calculate attack/defense score for character and monster
Shield gives more defense
Attack is function of class primary attribute and equipped weapon (and possibly bonus for having a pet or other special skill)
Need randomness - % chance of critical hit (bonus damage), % chance of critical failure (miss)
(Optional) instead of just clicking “attack”, have a form field where player guesses a number and the effectiveness of attack depends on how close that is to a randomly chosen number in a range
When you win, you get experience and loot (Items)
Penalty for losing -> you lose some experience, gold, loot
Option to flee, with random chance of success
In general, above calculations should be server-side, part of exposed API/routes (if done in JS, the user could edit/cheat)
(Optional) Figure out how to take into account click speed or similar to make an attack more effective
(Optional) Have special attacks, more complicated combat
Selling loot? Part of the optional “visit a shop after boss”
Goal/scoring
Experience - rewarded after defeating monster
Money - also rewarded after monster
Can only play as extended class after beating the game (or advancing sufficiently far) as a base class (and possibly increase game difficulty)
Back-end and front-end/visualization
Django-backed API (routes for CRUD operations on entities)
Some Django templating + React front-end that consumes data from API
(Optional) make it shinier/graphical (probably with JavaScript/CSS)


BRAINSTORM AREA BELOW
----------------------------------------

A posse of Fighter, Mage, Cleric and Thief that could open up to combo characters such as Assassin and Paladin.

The narrative is a posse will go down the road and handle any crisis that thrown at them.  
Aggressive NPC with sword - fire up our fighter character
Aggressive NPC with potions - fire up our Mage character
NPC who was attacked needing our healing - fire up our Cleric character
NPC who is wealthy and steals from the poor - fire up our Thief character
    
As story progress, can train special characters such as Assassin and/or Paladin to prepare when needed.

When the crisis is handled with success, receive items to improve the certain level of our character (i.e. our Fighter character wins fight with enemy fighter, our fighter character is awarded with additional level of rage).

Possibly add a randomizer for each attack to have a possible chance of a ‘critical hit’ which can do 1.5x the damage or even a “miss”

Provide special attacks that can be used when an attack bar reaches a certain level. Then depending on the attack, subtracts a certain amount of points from the attack bar.
Attack bar can increase from potions, victories, critical hits, etc.

Have a certain “coin-flip” mechanism to decide who gets to strike first

Weapon Upgrades that are persistent and gain certain special attacks and increased damage, etc

What if instead of clicks we used a “dice roll” from a range of 1 - 10 and the player guesses a number before the roll and if matches === critical hit. And the attack diminishes as it gets further away from the dice number rolled to a “miss”.



RESOURCES
-------------------------
https://msdn.microsoft.com/en-us/magazine/dn759441.aspx

https://github.com/thomcom/berserker


