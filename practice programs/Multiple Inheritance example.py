class Engine:
    def engine_info(self):
        print("Engine details")
class Body:
    def body_info(self):
        print("Body details")
class Car(Engine,Body):
    def car_info(self):
        print("This is a car")
car=Car()
car.engine_info()
car.body_info()
car.car_info()