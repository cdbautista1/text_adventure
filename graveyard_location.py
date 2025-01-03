import random
from weather import weather  # Importing the weather module
from items import warrior_items, mage_items, archer_items  # Importing items, weapons, armor, and potions modules

# Function that goes through what the player decides to do in the graveyard, with various outcomes based on weather
def graveyard(area, player_class):
    # Check if the player is in the graveyard
    if area == 'Graveyard':
        # Randomly choose the weather condition for the graveyard
        location_weather = random.choice(weather)

        # If the weather is rainy, execute this scenario
        if location_weather == 'rainy':
            print(
                f'As you make your way to the graveyard, dark clouds gather overhead, and a cold rain begins to fall. The path becomes slippery, and the air grows heavy with an unnatural chill. '
                'Through the sheets of rain, a dense fog rolls in, swallowing the gravestones one by one. Faint murmurs drift from the mist, haunting and otherworldly. '
                'With each step closer, the whispers grow louder. \nDo you walk "towards" the voices or "away" from them?'
            )

            while True:
                # Prompt the player for their choice
                user_input = input()
                if user_input == 'towards':
                    print(
                        'Summoning your courage, you venture further into the mist. As you approach, the whispers twist into sharp laughter, and skeletal figures begin to rise from the soaked earth. '
                        'Their empty eye sockets glow faintly, locking onto you.'
                    )
                    break  # Exit the loop if the player chooses to proceed

                elif user_input == 'away':
                    print(
                        'Overwhelmed by fear, you retreat toward the safety of the graveyard’s entrance. Whatever secrets lie within the mist will remain undiscovered—for now.'
                    )
                    print('Game Over.')
                    break  # Exit the loop if the player chooses to leave

                else:
                    print('The whispers seem to mock your hesitation. Choose either "towards" or "away".')

            # Define a function to handle the weapon choice after facing the skeletons
            def get_weapons(player_class):
                if player_class == 'Warrior':
                    weapons = warrior_items['weapons']
                elif player_class == 'Mage':
                    weapons = mage_items['weapons']
                elif player_class == 'Archer':
                    weapons = archer_items['weapons']

                # Randomly select two weapons from the available pool
                weapon_options = random.sample(weapons, 2)

                while True:
                    # Prompt the player for their weapon choice
                    weapon_choice = input(
                        f"Amid the chaos, you spot a discarded {weapon_options[0]} and {weapon_options[1]}. Which will you take to defend yourself? "
                    ).strip().lower()  # Normalize input by stripping spaces and making it lowercase

                    # Normalize weapon names for comparison
                    weapon_1 = weapon_options[0].lower()
                    weapon_2 = weapon_options[1].lower()

                    if weapon_choice == weapon_1 or weapon_choice == weapon_2:
                        print(f'You grip the {weapon_choice.title()} tightly, preparing to fight the skeletal horde.')
                        break  # Exit the loop after choosing a valid weapon
                    else:
                        print(f'Time is running out! Choose a valid weapon.')

            # Call the weapon selection function        
            get_weapons(player_class)

        # If the weather is sunny, execute this scenario    
        elif location_weather == 'sunny':
            print(
                f'Under a clear, sunny sky, the graveyard feels strangely alive. Birds sing in the distance, yet the air carries an unnatural stillness. '
                'Rows of weathered tombstones stretch before you, but one in particular catches your eye. Its name is oddly familiar, though you cannot place it. '
                'As you approach, a swirling mist gathers above the grave, forming into a translucent figure. '
                'The apparition gestures with shadowy hands, revealing two scrolls. "Before you lie two paths," it intones. '
                'The scroll in my "left" hand offers a test of wit with a reward of items or potions. The scroll in my "right" hand presents a trial by combat, with a reward of weapons or armor." '
                'The choice is yours."'
            )

            while True:
                # Prompt the player to choose between two scrolls
                scroll_choice = input('Choose either the "left" scroll or the "right" scroll from the apparition. ').lower()

                if scroll_choice == 'left':
                    print('You reach for the left scroll, and the figure dissolves into the mist.')

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

                            # **Change: Reward logic now happens only after completing the entire puzzle**
                            print("Congratulations traveler, you have successfully completed the puzzle!")

                            # **Only after the puzzle is completed do we handle the reward**
                            if player_class == 'Warrior':
                                possible_items = warrior_items['items']
                                possible_potions = warrior_items['potions']
                            elif player_class == 'Mage':
                                possible_items = mage_items['items']
                                possible_potions = mage_items['potions']
                            elif player_class == 'Archer':
                                possible_items = archer_items['items']
                                possible_potions = archer_items['potions']

                            random_potion = random.choice(possible_potions)
                            random_item = random.choice(possible_items)
                            reward_choice = input('As promised, your reward is the choice between an item or potion. ')

                            if reward_choice == 'item':
                                print(f'As promised, your reward is the {random_item}.')
                            elif reward_choice == 'potion':
                                print(f'As promised, your reward is the {random_potion}.')
                            else:
                                print(f'Choose an item, mortal.')

                elif scroll_choice == 'right':
                    print(
                        'You grasp the right scroll, and the apparition vanishes. Suddenly, a shadowy knight emerges, wielding a massive blade. The trial by combat begins!'
                    )
                    # Placeholder for combat scenario
                    break  # Exit the scroll loop choice

                else:
                    print('The apparition waits, its glowing eyes fixed on you. Choose "left" or "right".')
