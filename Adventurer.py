class Adventurer:
    def __init__(self):
        """Constructor that initialises an instance if type Adventurer. Since no arguments are passed in, the Adventurer is assigned an integer value of 5 for both
        its skill and will level. The inventory attribute is an empty list that is used to append item objects found throughout the game and the current_room attribute
        is a room object used to locate the Adventurer's position."""
        self.skill = 5
        self.will = 5
        self.inventory = []
        self.current_room = None

    def get_inv(self):
        """Returns the Adventurer's inventory (list of item objects)"""
        return self.inventory

    def get_skill(self):
        """Returns the adventurer's total skill level (with items equipped)"""
        return self.skill

    def get_will(self):
        """Returns the adventurer's total will power"""
        return self.will

    def take(self, item):
        """Appends a new item object to the Adventurers inventory (self.inventory) and updates the Adventurer's skill and will levels."""
        self.inventory.append(item)
        self.skill += item.skill_bonus
        if self.skill < 0:
            self.skill = 0
        self.will += item.will_bonus
        if self.will < 0:
            self.will = 0
        return

    def check_self(self):
        """Shows adventurer stats and all item stats."""
        print("You are an adventurer, with a SKILL of 5 and a WILL of 5.\nYou are carrying:\n".format(self.skill, self.will))
        if len(self.inventory) == 0:
            print("Nothing.\n")
        else:
            for item in range(len(self.inventory)):
                print(self.inventory[item].name)
                print("Grants a bonus of {} to SKILL.".format(self.inventory[item].skill_bonus))
                print("Grants a bonus of {} to WILL.\n".format(self.inventory[item].will_bonus))
        print("With your items, you have a SKILL level of {} and a WILL power of {}.".format(self.get_skill(), self.get_will()))