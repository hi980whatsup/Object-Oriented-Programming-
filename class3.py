#Write a program to create a class Parrot and perform the following tasks - Create a class variable species Create a __init__ method that has instance variables - name and age Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well

class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("name is", self.name, "age is", self.age)


object = Parrot("chucky", 5)

print("class variable is", object.species)

object.display()
