#Write a program to create a class with name Student and perform the following tasks - Create a class variable grade and name Create a function to print a sentence Create a function to print class variables grade and name Create an object of class Student Call the two functions to execute them

class Student:
    grade = "10"
    name = "Ferran Torres"
    
    def display(self):
        print("I want to be a football player!")
    
    def displaydetails(self):
        print("Grade and name is", self.grade, self.name)


object = Student()
object.display()
object.displaydetails()

