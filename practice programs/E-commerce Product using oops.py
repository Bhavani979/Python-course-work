class Product:
 discount = 5 # Class Attribute (default discount for all products)
 def __init__(self, name, price, quantity):
   self.name = name # Instance Attribute
   self.price = price
   self.quantity = quantity
 def apply_discount(self):
   """Instance Method: Applies discount to price"""
   self.price -= self.price * (self.discount / 100)
 @classmethod
 def update_discount(cls, new_discount):
  """Class Method: Updates discount for all products"""
  cls.discount = new_discount
 @staticmethod
 def is_available(quantity):
  """Static Method: Checks if product is available"""
  return quantity > 0
# Creating product instances
p1 = Product("Laptop", 50000, 10)
p2 = Product("Phone", 20000, 5)
# Applying discount
p1.apply_discount()
print(p1.price) # 47500 (5% discount applied)
# Updating discount for all products
Product.update_discount(10)
p2.apply_discount()
print(p2.price) # 18000 (10% discount applied)
# Checking product availability
print(Product.is_available(p1.quantity)) 