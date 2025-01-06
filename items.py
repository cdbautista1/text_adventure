class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, character):
        """Simulate using the item, applying its effect."""
        print(f"{character.name} uses {self.name}: {self.effect}")

    def __str__(self):
        """Return a user-friendly string representation of the item."""
        return self.name


# Warrior Items
warrior_items = {
    "items": [
        Item("Elixir of Battle Fury", "A flask filled with a potion that boosts attack power.", "Increases attack by 20% for 5 minutes."),
        Item("Rope of the Valiant", "A sturdy rope useful for climbing or tying enemies.", "Can be used to climb or bind targets."),
        Item("Bronze Warden's Key", "A key to open ancient, rusted doors.", "Unlocks locked doors or chests."),
        Item("Bag of the Brave", "A durable bag to carry essential items.", "Increases inventory space.")
    ],
    "weapons": [
        Item("Rusty Broadsword", "A tarnished relic of forgotten battles, its edge dulled by time.", "Provides modest attack power but lacks finesse."),
        Item("Blade of the Titan", "A mighty sword forged from the heart of a fallen giant.", "Increases attack by 10 and can stun enemies."),
        Item("Spear of the Storm King", "A long spear imbued with the power of the storm.", "Increases range and attack speed."),
        Item("Axe of the Blood Oath", "An axe bound by a warrior's blood pact.", "Deals high damage, but slows movement."),
        Item("Longbow of the Steelheart", "A bow crafted by the greatest blacksmiths.", "Increases critical hit chance by 15%.")
    ],
    "armor": [
        Item("Cooking Pot Lid", "A battered lid from an old cooking pot, repurposed as a makeshift shield.", "Offers minimal protection, but better than nothing."),
        Item("Aegis of the Champion", "A shield that grants immense protection.", "Increases defense by 25% and can block damage."),
        Item("Helm of the Iron Lord", "A helmet forged from iron and magic.", "Increases resistance to magic by 15%."),
        Item("Boots of the Unyielding", "Boots that increase movement speed and stability.", "Increases speed by 10%."),
        Item("Gauntlets of Fury", "Gauntlets that empower physical attacks.", "Increases strength and attack speed.")
    ],
    "potions": [
        Item("Vial of Fleetfoot’s Grace", "A potion that grants incredible speed.", "Increases movement speed by 30% for 10 minutes."),
        Item("Vial of Titan’s Might", "A potion that greatly enhances strength.", "Increases attack power by 30% for 5 minutes."),
        Item("Elixir of Ironbark Resilience", "A potion made from the bark of ancient trees.", "Reduces incoming damage by 20% for 5 minutes.")
    ]
}

# Mage Items
mage_items = {
    "items": [
        Item("Flask of Mystical Waters", "A flask filled with water drawn from enchanted springs.", "Restores 20% of health over 2 minutes."),
        Item("Rope of Arcane Binding", "A magical rope that can tie and bind enemies.", "Can immobilize enemies for 5 seconds."),
        Item("Key of the Forgotten Sanctum", "A key that unlocks the hidden rooms of an ancient sanctuary.", "Unlocks sealed areas or doors."),
        Item("Satchel of Arcane Wonders", "A magical bag filled with scrolls and magical trinkets.", "Increases spellcasting speed and mana recovery.")
    ],
    "weapons": [
        Item("Walking Staff", "A weathered wooden staff, worn smooth by countless journeys.", "Increases balance and offers a slight boost to spellcasting focus."),
        Item("Wand of Eternal Flame", "A wand that controls the power of fire.", "Increases fire spell damage by 20%."),
        Item("Spear of Arcane Fire", "A spear infused with arcane fire.", "Deals fire damage to multiple targets."),
        Item("Staff of Elemental Fury", "A staff that channels the elements.", "Increases elemental magic power by 25%."),
        Item("Bow of the Moonlight Arrows", "A bow that fires enchanted arrows under the moonlight.", "Increases magic damage of arrows.")
    ],
    "armor": [
        Item("Tattered Robes", "A threadbare set of robes that barely provides protection from the elements.", "Offers minimal defense but allows for unhindered movement."),
        Item("Arcane Shield of the Sorcerer", "A shield that offers protection against magical attacks.", "Increases defense against magic by 20%."),
        Item("Crown of the Spellweaver", "A crown that enhances the mage’s magical abilities.", "Increases spell power by 15%."),
        Item("Boots of the Moonlit Path", "Boots that increase movement speed under the moonlight.", "Increases speed by 15% at night."),
        Item("Gloves of the Magus", "Gloves that allow the mage to handle magical energies more easily.", "Increases mana regeneration by 10%.")
    ],
    "potions": [
        Item("Potion of Fleet Arcana", "A potion that enhances magical speed.", "Increases spell casting speed by 20% for 5 minutes."),
        Item("Potion of Titan’s Grasp", "A potion that increases magical strength.", "Increases magic damage by 25% for 5 minutes."),
        Item("Elixir of the Sage’s Vision", "A potion that grants clarity and foresight.", "Reveals hidden objects or enemies for 10 minutes.")
    ]
}

# Archer Items
archer_items = {
    "items": [
        Item("Flask of the Hunter’s Spirit", "A flask containing the essence of the hunter's focus.", "Increases critical hit chance by 15% for 10 minutes."),
        Item("Rope of Silent Shadows", "A rope that dampens sounds, useful for stealth.", "Can be used to escape or stealthily climb."),
        Item("Key of the Hidden Grove", "A key to unlock secret entrances in the forest.", "Unlocks hidden paths or entrances."),
        Item("Quiver Bag of the Lone Archer", "A quiver that enhances arrow capacity and organization.", "Increases arrow carrying capacity.")
    ],
    "weapons": [
        Item("Shortbow", "A simple, lightweight bow crafted for quick, precise shots.", "Increases attack speed but has limited range."),
        Item("Silverthorn Dagger", "A small but deadly dagger, forged from rare silverthorn.", "Increases attack speed and critical hit chance."),
        Item("Spear of the Silent Stalker", "A spear designed for stealth attacks.", "Increases damage when attacking from stealth."),
        Item("Axe of the Forest Guardian", "A powerful axe favored by guardians of the forest.", "Deals high damage to enemies in nature."),
        Item("Bow of the Wind Whisperer", "A bow made from ancient wood, favored by nature spirits.", "Increases range and damage in wooded areas.")
    ],
    "armor": [
        Item("Ripped Cowl", "A hood marred by wear and time, shrouding the wearer in anonymity.", "Enhances stealth but offers little protection."),
        Item("Cloak of the Shadow’s Veil", "A cloak that enhances stealth and hides the wearer in shadows.", "Increases stealth by 30%."),
        Item("Hood of the Phantom", "A hood that obscures the wearer's face and enhances vision.", "Increases stealth and night vision."),
        Item("Boots of the Swift Hunter", "Boots designed for swift movement and agility.", "Increases movement speed by 15%."),
        Item("Gloves of the Silent Strike", "Gloves that enhance precision and reduce noise.", "Increases attack precision and stealth attacks.")
    ],
    "potions": [
        Item("Potion of the Hunter’s Agility", "A potion that increases agility.", "Increases movement speed and attack speed by 15%."),
        Item("Potion of Bear’s Might", "A potion that boosts physical strength.", "Increases strength and melee damage by 25%."),
        Item("Vial of Woodland Strength", "A potion made from forest herbs that grants endurance.", "Reduces damage taken by 20% and increases stamina.")
    ]
}

