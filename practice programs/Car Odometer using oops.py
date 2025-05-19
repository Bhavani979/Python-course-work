class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
        self.odometer=0
    def drive(self,km):
        self.odometer+=km
    def show_odometer(self):
       print(f"Odometer:{self.odometer}")
car1=Car('Toyota','Innova')
car1.drive(100)
#car1.drive(30)
car1.show_odometer()