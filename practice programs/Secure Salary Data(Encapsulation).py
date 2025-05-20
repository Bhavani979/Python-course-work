class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
s=Employee(40000)
print(f"Salary:",s.get_salary())