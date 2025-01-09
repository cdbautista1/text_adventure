from graveyard_location import graveyard
from player_classes import Warrior, Mage, Archer
from graveyard_location import handle_departure

def run_graveyard_tests(player_class, class_name):
    print(f"\n=== Testing {class_name} ===")

    print(f"First visit to the graveyard ({class_name}):")
    graveyard('Graveyard', player_class)

    print(f"\nAttempt to return to the graveyard without visiting other areas ({class_name}):")
    graveyard('Graveyard', player_class)

    print(f"\nVisit the woods ({class_name}):")
    player_class.has_visited_woods = True  # Simulate visiting the woods

    print(f"\nReturn to the graveyard after visiting the woods ({class_name}):")
    graveyard('Graveyard', player_class)

    print(f"\nVisit the crypt ({class_name}):")
    player_class.has_visited_crypt = True  # Simulate visiting the crypt

    print(f"\nReturn to the graveyard after visiting the crypt ({class_name}):")
    graveyard('Graveyard', player_class)

# Create player instances
warrior = Warrior()
mage = Mage()
archer = Archer()

# Run tests for all classes
run_graveyard_tests(warrior, "Warrior")
run_graveyard_tests(mage, "Mage")
run_graveyard_tests(archer, "Archer")

