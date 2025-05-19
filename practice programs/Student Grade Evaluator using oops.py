class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def ispassed(self):
        avg=sum(self.marks)/len(self.marks)
        return avg>=40
s1=Student('Jannu',[45,78,90])
s2=Student('Akshaya',[40,30,46])
print(f"Passed:",s1.ispassed())
print(f"Passed:",s2.ispassed())
