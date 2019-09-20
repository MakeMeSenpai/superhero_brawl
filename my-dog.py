#Classes are modular, and can be reused in spereate files of your code
#this example imports from our file dogpy and inputs it here for us to use
import dog

my_other_dog = dog.dog("Annie", "Super dog!")
A_third_dog = dog.dog("Sparkie", "Human?!")
print("Oh no! my_dog has been exposed to radio activity and is now " + my_other_dog.name + " the " + my_other_dog.breed)
A_third_dog.sits()
A_third_dog.roll()
print("wow, " + A_third_dog.name + " is a really good boy. what kind of breed is it? Wait What?! It's a " + A_third_dog.breed)
dog.bark = "Woah!"
my_other_dog.bark()