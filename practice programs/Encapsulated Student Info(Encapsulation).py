class Student:
    def __init__(self,name):
        self.__name=name
    def get_info(self):
        return self.__name
s=Student("Julie")
print(f"Student name:",s.get_info())
