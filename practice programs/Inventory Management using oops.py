class Inventoryitem:
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity
    def updated_quantity(self,amount):
        self.quantity+=amount
    def show_quantity(self):
       print(f"{self.name}: {self.quantity} in stock")
item1=Inventoryitem("Tab",15000)
item1.updated_quantity(-5000)
item1.show_quantity()