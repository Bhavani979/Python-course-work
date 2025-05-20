# Parent Class
class Animal:
  def speak(self):
    print("Animals can make sounds.")

# Child Class inheriting from Animal
class Dog(Animal):
  def bark(self):
    print("Dog barks: Woof! Woof!")

# Creating an object of the Child Class
dog = Dog()
dog.speak() # Inherited method from Animal class
dog.bark() # Method specific to Dog class