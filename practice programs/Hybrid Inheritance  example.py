class Vehicle:
    def vehicle_info(self):
        print("Vehicle information.")
class Car(Vehicle):
    def car_info(self):
        print("Car details.")
class Electric:
    def battery_info(self):
        print("Battery details.")
class ElectricCar(Car,Electric):
   def eco_friendly(self):
      print("This is an eco-friendly car.")
tesla = ElectricCar()
tesla.vehicle_info()
tesla.car_info()
tesla.battery_info()
tesla.eco_friendly()


