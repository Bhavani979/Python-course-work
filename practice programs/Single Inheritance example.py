class Vehicle:
    def info(self):
        print("This is a vehicle")
class Car(Vehicle):
    def car_info(self):
        print("This is a car")
car=Car()
car.info()
car.car_info()