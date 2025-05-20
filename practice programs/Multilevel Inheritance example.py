class Grandparent:
    def show_grandparent(self):
        print("Grandparent class")
class Parent(Grandparent):
    def show_parent(self):
        print("Parent class")
class Child(Parent):
    def show_child(self):
        print("Child class")
c=Child()
c.show_grandparent()
c.show_parent()
c.show_child()