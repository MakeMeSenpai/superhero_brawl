import random


class Ability():
    def __init__(self, name, attack_strength=20):
        self.name = name  # str
        self.max_damage = attack_strength  # int

        # creates random attack value
    def attack(self):
        return random.randint(0, self.max_damage)


class Armor():
    def __init__(self, name, max_block=20):
        self.name = name  # str
        self.max_block = max_block #int

    # creates random block value
    def block(self):
        return random.randint(0, self.max_block)


class Hero():
    def __init__(self, name, starting_health=100):
        self.name = name  # str
        self.starting_health = starting_health  # int
        self.current_health = self.starting_health  # int
        self.abilities = []
        self.armors = []

    # adds a new ability to self.abilities list
    def add_ability(self, ability):
        #new_ability = input("What's your new ability? ")
        return self.abilities.append(ability)

    def add_armor(self, armor):
        return self.armors.append(armor)

    # adds ability values together to get attack value
    def attack(self):
        attack_value = 0
        for ability in self.abilities:
            attack_value += ability.attack()
        return attack_value

    def defend(self, incoming_damage):
        defended = incoming_damage
        for armor in self.armors:
            defended += armor.block()
        return defended

    def take_damage(self, incoming_damage):
        self.current_health -= self.defend(incoming_damage)
        
    def is_alive(self):
        if self.current_health <= 1:
            return False
        else:
            return True
        pass

    def fight(self, opponent):  # opponent == hero class
        # TODO: Fight each hero until a victor emerges.
        # Print the victor's name to the screen.
        while self.is_alive():
            if opponent == self:
                return "Draw!"
            else: 
                winner = self
                return winner


# tests your code!
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # help from jess as to how to let the user input their own abilities!
    # you made the mistake of giving that option too early inside the function
    # therefore creating a string instead of an object! strings are just "words"
    # while objects are sorta like dictionaries in which each key holds it's own values
    #ability_name = input("Enter a name")
    # attack value = int(input("Enter a value"))
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)