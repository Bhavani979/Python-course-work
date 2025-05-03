class Batch:
    batchno=22
    @classmethod
    def setbatchno(cls,new_batch):
        cls.batchno=new_batch
        print(cls.batchno,"Inside the cls method")
    def setdetails(self,name,course):
        self.name=name
        self.course=course
    def display(self):
        print(f'Welcome to {self.course} course {self.name} {Batch.batchno}')
    @staticmethod
    def fee():
        return '50k'
Bhavani=Batch()
Pavani=Batch()
Bhavani.setdetails("Bhavani","Python")
Pavani.setdetails("Pavani","Java")
Bhavani.name="Akshaya"
Bhavani.display()
Pavani.display()
print(Batch.batchno)
Batch.setbatchno(26)
print(Batch.fee())