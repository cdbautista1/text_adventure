import random
from weather import weather
from items import warrior_items, mage_items, archer_items
from player_classes import Warrior, Mage, Archer


# function that goes through what the user decides to do in the woods
def woods(area, player_class):
    if area == 'Woods':     
        print('You enter the woods, where birdsong and rustling leaves create a lively backdrop. The towering trees form a dense canopy,' 
              'and shafts of moonlight peek through the branches. As you cut through the undergrowth, your eyes catch sight of two treasure'
              'chests nestled in a small clearing. Their metal edges glint faintly, as if beckoning you to choose. As you prepare to make your choice, a subtle shift in the air '
              'hints that something will change once you decide. You feel the weight of your choice, knowing that whatever you uncover will guide you deeper into the woods.'
        )
        
    choose_chest(player_class.name)

def choose_chest(player_class):
        if player_class == 'Warrior':
            items = warrior_items['items']
        elif player_class == 'Mage':
            items = mage_items['items']
        elif player_class == 'Archer':
            items = archer_items['items']
        else:
            print('Unknown player class.')
            return

        while True:
            chest_choice = input('Choose either the "left" or "right" treasure chest to open. ').strip().lower()
            
            if chest_choice == 'left':
                chosen_item = random.choice(items)
                print(f'You chose the left treasure chest. As you open it, you feel a shift in the air, and {chosen_item} appears in your hands.')
                break

            elif chest_choice == 'right':
                chosen_item = random.choice(items)
                print(f'You chose the right treasure chest. The moment you open it, the air changes, and you find {chosen_item} inside.')
                break
            
            else:
                print('Invalid choice. Please choose either "left" or "right".')

            
        location_weather = random.choice(weather)
        
        if location_weather == 'rainy':
            handle_rainy_weather(player_class)
        elif location_weather == 'sunny':
            handle_sunny_weather(player_class)
        else:
            print('Unexpected weather.')



def describe_rainy_weather():
    print('A steady rain begins to fall, turning the ground beneath your feet into a slippery, ' 
          'muddy mess. The vibrant sounds of wildlife fade into the background, drowned out by the steady drumming of rain on the trees.'
    )
    print('The night sky grows darker, and the once peaceful air is now thick with the scent of wet earth and rain-soaked bark. As you continue, '
          'through the misty rain, you spot a rainbow arching across the sky. It\'s an unexpected sight in the night, the brilliant colors standing out against the gray clouds.')
    print('The arc seems to guide you forward, its presence surreal amidst the downpour. You follow the rainbows path, and soon, you find a plaque half-covered by the rain at the base of an ancient tree.'

          '\n The riddle reads:'

          '\n “I rise from the earth when the sky weeps,'
          '\n I bloom and fade in the light it keeps.'
          '\n Though I\'m fleeting, I paint the sky,'
          '\n A bridge of color, soaring high.”'
          '\n What am I? Think carefully and choose your answer.'

    )


def describe_sunny_weather():
    print('The clouds suddenly part, and to your astonishment, the night gives way to the bright warmth of the sun. The transformation is abrupt—what was once a dark, ' 
          'quiet night is now filled with the vibrant golden light of day. The air is fresh, carrying the scent of drying earth, and the shadows cast by the towering trees stretch long across '
          'the forest floor. Despite the previous chill of the night, the sunlight now floods the woods, making the surroundings feel alive and warm. '

          'You notice the shadows growing longer, more defined, following your every step. A faint glow catches your eye—at the base of an ancient tree, a small plaque is partially hidden among the roots. '
          '\n The inscription reads:'

          '\n “I hide at noon but stretch at dawn,'
          '\n I follow you, but I am never gone.'
          '\n I am a form, but no solid shape,'
          '\n A darkened twin, I twist and scrape.”'
          '\n Take a moment to ponder the riddle and give your answer.'
    )


def handle_rainy_weather(player_class):
    describe_rainy_weather()
    rainy_riddle()


def handle_sunny_weather(player_class):
    describe_sunny_weather()
    sunny_riddle()


def rainy_riddle():
    print('test rainy riddle')


def sunny_riddle():
    ('test sunny riddle')