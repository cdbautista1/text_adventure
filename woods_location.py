import random
from items import warrior_items, mage_items, archer_items


# function that goes through what the user decides to do in the woods
def woods(area):
    if area == 'Woods':     
        print('You chose the woods. You hear the constant sounds of birds and other woodland creatures in the distance. As you cut through branches and climb over '
              'bushes, you spot two treasure chests sitting in the middle of a field, illuminated by the moonlight.')

        while True:
            chest_choice = input('Choose either the "left" or "right" treasure chest to open. ')
            
            if chest_choice == 'left':
                chosen_item = random.choice(random.choice([warrior_items]))
                print(f'You chose the left treasure chest and received {chosen_item}.')
                break

            elif chest_choice == 'right':
                chosen_item = random.choice(random.choice([warrior_items]))
                print(f'You chose the right treasure chest and received {chosen_item}.')
                break
            
            else:
                print('Invalid choice. Please choose either "left" or "right".')

        print('You continue on your way')
