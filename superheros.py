import random

class Ability():
    def __init__(self, name, attack_strength):
        self.name = name #str
        self.max_damage = 20 #attack_strength #int

            #creates random attack value
    def attack(self):
        return random.randint(0,self.max_damage)

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
    
    def add_ability(self, ability):
        new_ability = input("What's your new ability? ")
        return self.abilities.append(new_ability)

    #TODO: Create The Attack Method- func should interate over abilities list calling Ability.attack() 
    #for each ability in the list. Than add together all the randint values together to determine full
    #damage. (test is already included)
    def attack(self):
        count = 0
        for num in self.abilities:
            count += 1 
        return Ability.attack(count)

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
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())