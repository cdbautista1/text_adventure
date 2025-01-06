import random
from weather import weather  # Importing the weather module
from items import warrior_items, mage_items, archer_items  # Importing items, weapons, armor, and potions modules


def graveyard(area, player_class):
    if area == 'Graveyard':
        if player_class.has_visited_woods or player_class.has_visited_crypt:
            # Randomly choose the weather condition for the graveyard
            location_weather = random.choice(weather)

            # Call function based on weather 
            if location_weather == 'rainy':
                handle_rainy_weather(player_class)
            elif location_weather == 'sunny':
                handle_sunny_weather(player_class)
            else:
                print('Unexpected weather condition')


def describe_rainy_weather():
    print(
        f'As you make your way to the graveyard, dark clouds gather overhead, and a cold rain begins to fall. The path becomes slippery, and the air grows heavy with an unnatural chill. '
        'Through the sheets of rain, a dense fog rolls in, swallowing the gravestones one by one. Faint murmurs drift from the mist, haunting and otherworldly. '
        'With each step closer, the whispers grow louder. \nDo you walk "towards" the voices or "away" from them?'
    )


def choose_weapon(player_class):
    if player_class == 'Warrior':
        weapons = warrior_items['weapons']
    elif player_class == 'Mage':
        weapons = mage_items['weapons']
    elif player_class == 'Archer':
        weapons = archer_items['weapons']

    weapon_options = random.sample(weapons, 2)

    print(f'You have found two weapons: a {weapon_options[0]} and a {weapon_options[1]}. Which will you take to defend yourself?')

    weapon_choice = input().strip().lower()

    if weapon_choice in [weapon_options[0].lower(), weapon_options[1].lower()]:
        print(f'You grip the {weapon_choice.title()} tightly, preparing to fight the skeleton horde.')
    else: 
        print('You hesitate for too long, and the skeletons draw closer. You must act quickly!')


def handle_rainy_weather(player_class):
    describe_rainy_weather()
    user_input = input('Do you want to walk "towards" or "away" from them?')

    if user_input == 'towards':
        print(
            'Summoning your courage, you venture further into the mist. As you approach, the whispers twist into sharp laughter, and skeletal figures begin to rise from the soaked earth. '
            'Their empty eye sockets glow faintly, locking onto you.'
        )

        choose_weapon(player_class)


    elif user_input == 'away':
        print(
            'Overwhelmed by fear, you retreat toward the safety of the graveyard’s entrance. Whatever secrets lie within the mist will remain undiscovered—for now.'
        )
        print('Game Over.')

    else:
        print('The whispers seem to mock your hesitation. Choose either "towards" or "away".')


def handle_sunny_weather(player_class):
    pass


def handle_away(player_class):
    # Check if the player has visited another area
    if player_class.has_visited woods or player_class.has_visited crypt:
        # Allow the player to return to the graveyard
        print('You have returned to the graveyard after visiting other areas.')
        player_class.has_visited_graveyard = True
    else:
        print('You can\'t return to the graveyard just yet. Try exploring the woods or the crypt first.' )
    pass
