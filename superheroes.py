import random

random.choice 
class Ability():
    def __init__(self, name, attack_strength=20):
        self.name = name  # str
        self.max_damage = attack_strength  # int

    # creates random attack value
    def attack(self):
        return random.randint(0, self.max_damage)

class Weapon(Ability):
    #returns a weaker attack when hero uses a weapon. 
    def attack(self):
        weapon_damage = random.randint(self.max_damage//2, self.max_damage) 
        return weapon_damage

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
        self.deaths = 0
        self.kills = 0

    # adds a new ability to self.abilities list
    def add_ability(self, ability):
        #new_ability = input("What's your new ability? ")
        return self.abilities.append(ability)

    # adds a new set of armor to self.armors list
    def add_armor(self, armor):
        return self.armors.append(armor)

    # adds ability values together to get attack value
    def attack(self):
        attack_value = 0
        for ability in self.abilities:
            attack_value += ability.attack()
        return attack_value

    #returns total defense (Thank You George for the help in reunderstanding this funct purpose!)
    def defend(self):
        defended = 0
        for armor in self.armors:
            defended += armor.block()
        return defended

    #removes health from attaked hero
    def take_damage(self, incoming_damage):
        # takenDamage = incoming_damage - self.defend()
        # print(f'took {takenDamage} dmg')
        # self.current_health -= takenDamage
        # print(f'current health:  {self.current_health}')
        defend = self.defend()
        dmg = incoming_damage - defend
        self.current_health -= dmg

    #checks if heros are still alive      
    def is_alive(self):
        if self.current_health > 0:
            return True
        return False

    #determines if heros have different level of abilities, and determines a winner
    def fight(self, opponent):  # opponent == hero class
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            return "Draw!"
        while True:  
            if self.is_alive():
                dmg = self.attack()
                opponent.take_damage(dmg)
            else: 
                opponent.add_kills(1)
                self.add_deaths(1)
                break

            if opponent.is_alive():
                dmg = opponent.attack()
                self.take_damage(dmg)
            else: 
                self.add_kills(1)
                opponent.add_deaths(1)
                break
        #TODO: Refactor this method to update the
        # number of kills the hero has when the opponent dies. 
        # Also update the number of deaths for whoever dies in the fight  

    #Update kills with num_kills
    def add_kills(self, num_kills):
        self.kills += num_kills

    #Update deaths with num_deaths
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths


class Team():
    def __init__(self, name):
        self.name = name
        self.heroes = []

    #adds hero object to self.heroes list
    def add_hero(self, Hero):
        self.heroes.append(Hero)
    
    #removes hero object from self.heroes list, or 0 if hero is not found
    def remove_hero(self, name):
        if name in self.heroes:
            return self.heroes.remove(name)
        else:
            return 0
    
    #prints out all heros in console
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def alive_heroes(self):
        return [x for x in self.heroes if x.is_alive()]

    #Battle each team against each other.
    def attack(self, other_team):
        # for person in self.heroes:
        #     if person.is_alive():
        #         super_hero = random.choice(self.heroes)
        #         villain = random.choice(other_team.heroes)
        #         super_hero.fight(villain)

        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            self_champ = random.choice(self.alive_heroes())
            opp_champ = random.choice(other_team.alive_heroes())
            self_champ.fight(opp_champ)

        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.

    #Reset all heroes health to starting_health
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
        # TODO: This method should reset all heroes health to their
        # original starting value.

    #Print team statistics  
    def stats(self):
        for hero in self.heroes:
            print(f'''{hero.name}; HP: {hero.current_health}:{hero.starting_health} AC: 
            {hero.abilities} DC: {hero.armors} KD: {hero.kills}:{hero.deaths}''')
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        pass

# tests your code!
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # help from jess as to how to let the user input their own abilities!
    # you made the mistake of giving that option too early inside the function
    # therefore creating a string instead of an object! strings are just "words"
    # while objects are sorta like dictionaries in which each key holds it's own values
    # ability_name = input("Enter a name")
    # attack value = int(input("Enter a value"))
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    #weapon1 = Weapon("Hammer", 50)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)

# superheroes.py:126: in attack
#   self.fight(opponent)
# superheroes.py:78: in fight
#   while self.is_alive():
# Thanks Ben 