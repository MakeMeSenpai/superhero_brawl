import random

class Ability():
    def attack(self):
        def __init__(self, name, attack_strength):
            self.name = name #str
            self.max_damage = 20 #attack_strength #int

            #creates random attack value
            def attack(self):
                attack_value = random.randint(0,self.max_damage)
                return attack_value

        #TODO: Fix abilities test, this a requirement, this applies to all functions :/
        # if __name__ == "__main__":
        # # If you run this file from the terminal
        # # this block is executed.
        # ability = Ability("Debugging Ability", 20)
        # print(ability.name)
        # print(ability.attack())

class Armor():
    def __init__(self, name, max_block):
        self.name = name #str
        self.max_block = 20 #max_block #int

        #creates random block value
        def block(self):
            block_value = random.randint(0, self.max_block)
            return block_value

class Hero():
    def __init__(self, name, starting_health=100):
        self.name = name #str
        self.starting_health = starting_health #int
        self.current_health = 100 #int
        self.abilities = []
        self.armors= []
        pass

        # TODO: Just another test to fix
        # if __name__ == "__main__":
        # # If you run this file from the terminal
        # # this block is executed.
        # my_hero = Hero("Grace Hopper", 200)
        # print(my_hero.name)
        # print(my_hero.current_health)

        def add_ability(self, ability):
            new_ability = input("What's your new ability? ")
            self.abilities.append(new_ability)
            return self.abilities

        # TODO: And another test
        # if __name__ == "__main__":
        # # If you run this file from the terminal
        # # this block is executed.
        # ability = Ability("Great Debugging", 50)
        # hero = Hero("Grace Hopper", 200)
        # hero.add_ability(ability)
        # print(hero.abilities)

        def attack(self):
            pass

        def defend(self, incoming_damage):
            pass

        def take_damage(self):
            pass

        def is_alive(self):
            pass

        def fight(self, opponent): #opponent == hero class
            pass
