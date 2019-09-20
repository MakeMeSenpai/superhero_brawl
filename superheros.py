class ability():
    def __init__(self, name, max_damage):
        self.name = name #str
        self.max_damage = max_damage #int

        def attack():
            pass

class armor():
    def __init__(self, name, max_block):
        self.name = name #str
        self.max_block = max_block #int
    
        def block():
            pass

class hero():
    def __init__(self, name, starting_health):
        self.name = name #str
        self.starting_health = 100 #int

        def add_ability(ability_object):
            pass

        def attack():
            pass

        def defend(incoming_damage):
            pass

        def take_damage():
            pass

        def is_alive():
            pass

        def fight(opponent): #opponent == hero class
            pass