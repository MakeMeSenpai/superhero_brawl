class dog():
    #object init (the constructor.js of python)
    def __init__(self, name, breed):
        #init variables
        self.name = name
        self.breed = breed
    
    #instance method (doggo bark)
    def bark(self):
        print("Woof!")

    def roll(self):
        print(self.name + " rolled over!")

    def sits(self):
        count = 0 
        for count in range(2):
            if count == 0:
                print(self.name + " sat down!")
                count = 1
                return count
            else:
                print(self.name + " stood up!")
                count = 0
                return count

        

  
my_dog = dog("Rex", "German Sheppard")
print(my_dog)
print(my_dog.name)
print(my_dog.breed)
my_dog.breed = "Super Dog!"
my_dog.bark()
