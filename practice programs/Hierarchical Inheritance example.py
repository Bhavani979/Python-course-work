class Animal:
    def speak(self):
        print("Animals make sounds")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Cat(Animal):
    def meow(self):
        print("Cat meows")
dog=Dog()
cat=Cat()

dog.speak()
dog.bark()
 
cat.speak()
cat.meow()