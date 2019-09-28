class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{} is eating'.format(self.name))

    def drink(self):
        print('{} is drinking'.format(self.name))
        
    def sleep(self):
        print('{} is sleeping'.format(self.name))

if __name__ == "__main__":
    Kitty = Animal("Charollete")
    Kitty.eat()
    Kitty.drink()
    Kitty.sleep()