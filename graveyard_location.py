import random
from weather import weather  # Importing the weather module
from items import warrior_items, mage_items, archer_items  # Importing items for classes
from player_classes import Warrior, Mage, Archer  # Importing player classes


def graveyard(area, player_class):
    # Main function for the graveyard area.
    # Determines the weather and handles interactions based on player's progress.
    
    if area == 'Graveyard':
        # First time entering the graveyard
        if not player_class.has_visited_graveyard:
            player_class.has_visited_graveyard = True  # Mark it as visited

            location_weather = random.choice(weather)  # Randomly choose the weather condition for the graveyard
            if location_weather == 'rainy':
                handle_rainy_weather(player_class)
            elif location_weather == 'sunny':
                handle_sunny_weather(player_class)
            else:
                print('Unexpected weather condition.')

        # If they have already visited the graveyard
        else:
            # Check if they've visited other areas (Woods or Crypt)
            if player_class.has_visited_woods or player_class.has_visited_crypt:
                # Randomly choose the weather condition for the graveyard
                location_weather = random.choice(weather)

                # Call function based on weather
                if location_weather == 'rainy':
                    handle_rainy_weather(player_class)
                elif location_weather == 'sunny':
                    handle_sunny_weather(player_class)
                else:
                    print('Unexpected weather condition.')
            else:
                print('You cannot return to the graveyard yet. Try exploring the woods or the crypt first.')
                handle_away(player_class)



def describe_rainy_weather():
    # Describes the graveyard in rainy weather conditions.
    print(
        'As you make your way to the graveyard, dark clouds gather overhead, and a cold rain begins to fall. '
        'The path becomes slippery, and the air grows heavy with an unnatural chill. '
        'Through the sheets of rain, a dense fog rolls in, swallowing the gravestones one by one. '
        'Faint murmurs drift from the mist, haunting and otherworldly. With each step closer, the whispers grow louder.'
    )

def handle_rainy_weather(player_class):
    # Handles the scenario when the graveyard has rainy weather.
    describe_rainy_weather()
    user_input = input('Do you want to walk "towards" or "away" from them? ').strip().lower()

    if user_input == 'towards':
        print(
            'Summoning your courage, you venture further into the mist. As you approach, the whispers twist into sharp laughter, '
            'and skeletal figures begin to rise from the soaked earth. Their empty eye sockets glow faintly, locking onto you.'
        )
        choose_weapon(player_class.name)

    elif user_input == 'away':
        print(
            'Overwhelmed by fear, you retreat toward the safety of the graveyard’s entrance. Whatever secrets lie within the mist '
            'will remain undiscovered—for now.'
        )
        handle_departure(player_class)

    else:
        print('The whispers seem to mock your hesitation. Choose either "towards" or "away".')


def choose_weapon(player_class_name): # Function for "towards" input
    # Presents the player with a choice between two random weapons based on their class.
    if player_class_name == 'Warrior':
        weapons = warrior_items['weapons']
    elif player_class_name == 'Mage':
        weapons = mage_items['weapons']
    elif player_class_name == 'Archer':
        weapons = archer_items['weapons']
    else:
        print("Unknown player class. No weapons available.")
        return

    weapon_options = random.sample(weapons, 2)
    print(f'You have found two weapons: {weapon_options[0]} and {weapon_options[1]}. Which will you take to defend yourself?')

    weapon_choice = input().strip().lower()

    if weapon_choice in [weapon.name.lower() for weapon in weapon_options]:
        print(f'You grip the {weapon_choice.title()} tightly, preparing to face the skeleton horde.')
    else:
        print('You hesitate for too long, and the skeletons draw closer. You must act quickly!')


def handle_departure(player_class):
    # Handles the scenario when the player decides to leave the graveyard
    print(
        "As you turn your back on the graveyard, an unsettling chill follows you, as though the spirits are watching your retreat. "
        "The path back feels longer, the shadows deeper, and the silence heavier. Each step echoes with a sense of unfinished business, "
        "the whispers of the graveyard fading but never truly gone.\n"
        "\nYou can't shake the feeling that you’ve left something behind—something important. But for now, you resolve to explore elsewhere, "
        "hoping to grow stronger or uncover answers that might prepare you for whatever awaits in that cursed place."
    )

    # Marks the player as having left the graveyard
    player_class.has_visited_graveyard = True


def handle_sunny_weather(player_class):
    # Handles the scenario when the graveyard has sunny weather.
    print(
        f'Under a clear, sunny sky, the graveyard feels strangely alive. Birds sing in the distance, yet the air carries an unnatural stillness. '
        'Rows of weathered tombstones stretch before you, but one in particular catches your eye. Its name is oddly familiar, though you cannot place it. '
        'As you approach, a swirling mist gathers above the grave, forming into a translucent figure. '
        'The apparition gestures with shadowy hands, revealing two scrolls. "Before you lie two paths," it intones. '
        'The scroll in my "left" hand offers a test of wit with a reward of items or potions. The scroll in my "right" hand presents a trial by combat, with a reward of weapons or armor. '
        'The choice is yours."'
    )

    while True:
        left_or_right = input('Choose either the "left" or the "right" scroll. ').strip().lower()

        if left_or_right == 'left':
            left_scroll(player_class)
            break
        elif left_or_right == 'right':
            print('You grasp the right scroll, and the apparition vanishes. Suddenly, a shadowy knight emerges, wielding a massive blade. The trial by combat begins!')
            # combat functionality
            break
        else:
            print('The apparition waits, its glowing eyes fixed on you. Choose "left" or "right".')


def play_puzzle(player_class):
# Define the correct sequence of symbols
    correct_sequence = ['moon', 'flame', 'sword', 'skull']

    # Keep track of progress
    player_progress = 0

    # Loop for the puzzle
    while player_progress < len(correct_sequence):
        # Prompt player for input
        player_guess = input(f'Enter the {player_progress + 1} symbol (options: moon, flame, sword, skull): ').lower()

        # Check if the guess is correct
        if player_guess == correct_sequence[player_progress]:
            print(f'Correct! You unlocked symbol {player_progress + 1}.')
            player_progress += 1  # Move to the next symbol

        else:
            print('Wrong symbol! A trap activates! Progress has been set back one.')
            player_progress = max(0, player_progress - 1)  # Apply a penalty here, but ensure it doesn't go below 0   

    print("Congratulations traveler, you have successfully completed the puzzle!")

    if isinstance(player_class, Warrior):
        possible_items = warrior_items['items']
        possible_potions = warrior_items['potions']

    elif isinstance(player_class, Mage):
        possible_items = mage_items['items']
        possible_potions = mage_items['potions']

    elif isinstance(player_class, Archer):
        possible_items = archer_items['items']
        possible_potions = archer_items['potions']

    else:
        print('Unknown class.')
        return

    random_potion = random.choice(possible_potions)
    random_item = random.choice(possible_items)
    reward_choice = input('As promised, your reward is the choice between an item or potion. ')

    if reward_choice == 'item':
        print(f'You have chosen the {random_item} as your reward.')
    elif reward_choice == 'potion':
        print(f'You have chosen the {random_potion} as your reward.')
    else:
        print(f'Choose an item, mortal.')


def left_scroll(player_class):
    print('You reach for the left scroll, and the apparition dissolves into the mist.')
    print('The air around you grows colder, and the faintest sound of an ancient door creaking open can be heard in the distant.')

    # Call the function to handle the puzzle
    play_puzzle(player_class)


def right_scroll(player_class):
    print('You grasp the right scroll, and the apparition vanishes. Suddenly, a shadowy knight emerges, wielding a massive blade. The trial by combat begins!')


def handle_away(player_class):

    print(f'Has visited woods: {player_class.has_visited_woods}')
    print(f'Has visited crypt: {player_class.has_visited_crypt}')

    # Handles the case where the player tries to return to the graveyard without visiting other areas.
    if player_class.has_visited_woods or player_class.has_visited_crypt:
        print('You have returned to the graveyard after visiting other areas.')
    else:
        print('You cannot return to the graveyard yet. Try exploring the woods or the crypt first.')
