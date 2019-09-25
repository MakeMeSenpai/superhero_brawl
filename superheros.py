import random

class Ability():
    def __init__(self, name, attack_strength=20):
        self.name = name #str
        self.max_damage = attack_strength #int

            #creates random attack value
    def attack(self):
        return random.randint(0, self.max_damage)

class Armor():
    def __init__(self, name, max_block):
        self.name = name #str
        self.max_block = 20 #max_block #int

    #creates random block value
    def block(self):
        return random.randint(0, self.max_block)

class Hero():
    def __init__(self, name, starting_health=100):
        self.name = name #str
        self.starting_health = starting_health #int
        self.current_health = 100 #int
        self.abilities = []
        self.armors= []
    
    #adds a new ability to self.abilities list
    def add_ability(self, ability):
        #new_ability = input("What's your new ability? ")
        return self.abilities.append(ability)

    #adds ability values together to get attack_value
    def attack(self):
        for ability in self.abilities:
            attack_value += ability.attack()
        return attack_value

    def defend(self, incoming_damage):
        pass

    def take_damage(self):
        pass

    def is_alive(self):
        pass

    def fight(self, opponent): #opponent == hero class
        pass

#tests your code!
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    #help from jess as to how to let the user input their own abilities!
    #you made the mistake of giving that option too early inside the function
    #therefore creating a string instead of an object! strings are just "words"
    #while objects are sorta like dictionaries in which each key holds it's own values
    #ability_name = input("Enter a name")
    #attack_value = int(input("Enter a value"))
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())