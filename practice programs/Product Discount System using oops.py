class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def discount(self,percent):
        self.price-=self.price*(percent/100)
    def show_price(self):
        print(f"Discounted price:{self.price}")
p1=Product("Laptop",20000)
p1.discount(10)
p1.show_price()