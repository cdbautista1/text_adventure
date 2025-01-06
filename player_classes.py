class Warrior:
    def __init__(self):
        self.name = 'Warrior'
        self.health = 100
        self.attack = 20
        self.magic = 0
        self.defense = 10
        self.equipment = {'weapon': 'Rusty Broadsword', 'armor': 'Cooking Pot Lid'}
        self.has_visited_graveyard = False
        self.has_visited_woods = False
        self.has_visited_crypt = False

class Mage:
    def __init__(self):
        self.name = 'Mage'
        self.health = 60
        self.attack = 2
        self.magic = 18
        self.defense = 3
        self.equipment ={'weapon': 'Walking Staff', 'armor': 'Tattered Robes'}
        self.has_visited_graveyard = False
        self.has_visited_woods = False
        self.has_visited_crypt = False

class Archer:
    def __init__(self):
        self.name = 'Archer'
        self.health = 75
        self.attack = 15
        self.magic = 5
        self.defense = 5
        self.equipment = {'weapon': 'Shortbow', 'armor': 'Ripped Cowl'}
        self.has_visited_graveyard = False
        self.has_visited_woods = False
        self.has_visited_crypt = False