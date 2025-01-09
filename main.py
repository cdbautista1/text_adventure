
# create rarities on items
# create an inventory function
# finish graveyard, combat last


import random
from graveyard_location import graveyard
from crypt_location import crypt
from woods_location import woods
from items import warrior_items, mage_items, archer_items
from weather import weather  
from player_classes import Warrior, Mage, Archer     

def choose_player_class():
    print('Hail traveler. The road ahead is treacherous, and you must decide how best to face the dangers that await.')
    print('Will you walk the path of strength as a Warrior, command the arcane as a Mage, or strike from the shadows as an Archer?')
    while True:
        player_class = input("Choose your class (Warrior, Mage, Archer): ").capitalize()
        if player_class == 'Warrior':
            print('You are a Warrior, forged in the fires of battle. With strength unmatched and a will of iron, you stand at the forefront, '
                  'cleaving enemies with mighty blows. Your armor clinks as you adjust your grip on your weapon, ready for the trials ahead.')
            return Warrior()

        elif player_class == 'Mage':
            print('You are a Mage, a master of the arcane arts. The elements bend to your will, and your knowledge grants you power beyond the reach of mortal strength.'
            'The hum of latent energy surrounds you as you prepare your spells for the coming storm.')
            return Mage()

        elif player_class == 'Archer':
            print('You are an Archer, swift and precise. From the shadows, you rain death upon your foes with unerring accuracy. The pull of your bowstring is your '
                  'symphony, and your arrows sing of justice—or vengeance.')
            return Archer()

        else:
            print('Your destiny lies in your choice. Choose wisely: Warrior, Mage, or Archer.')

def choose_area():
    while True:
        area = input('Choose your path (Graveyard, Woods, Crypt) or type "exit" to exit: ').strip().lower()
        if area in ['graveyard', 'woods', 'crypt']:
            return area.capitalize()
        
        elif area == 'exit':
            return area
        
        else:
            print('Choose one of the three options.')

start_of_game = """In the darkening dusk, you find yourself at the edge of an ancient kingdom, its spires looming ominously in the distance. 
The path to the castle, where the King awaits your presence, is shrouded in mystery. Ahead of you, three distinct paths beckon, each fraught with danger and discovery.
To your left lies the **Graveyard**, its towering tombstones and twisted trees casting long shadows. A chilling breeze whispers through the old stone, telling tales of those long forgotten.
The middle path, the **Woods**, is dense with ancient trees, their gnarled roots entangling the ground like the fingers of the dead. Strange noises drift from within, and the scent of pine and earth fills the air.
To the right, the **Crypt** stands foreboding, its stone archway darkened by the overgrowth of moss and vines. Legends speak of forgotten treasures buried deep within, though many who sought them never returned.
Only one path can lead you to the King, but which one will you choose?"""

areas = ['Graveyard', 'Woods', 'Crypt', 'Castle']

player_class = choose_player_class()
print('\n')

print(start_of_game)
path = choose_area()

if path == 'Graveyard':
    graveyard(path, player_class)
elif path == 'Woods':
    woods(path, player_class)
elif path == 'Crypt':
    crypt(path, player_class)