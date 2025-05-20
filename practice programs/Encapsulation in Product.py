class Product:
    def __init__(self):
        self.__stock=100
    def buy(self,quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
        else:
            print("Out of stock")
    def check__stock(self):
        return self.__stock
s=Product()
s.buy(120)
s.buy(20)
print(s.check__stock())
