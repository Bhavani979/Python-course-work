class Batch:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def login(self):
        if self.username and self.password:
            print("Login successful",self.username)
        else:
            print("Enter the username and password correctly",self.username)
bhavani=Batch("bhavani","bhavani@123")
akshaya=Batch("akshaya","")
bhavani.login()
akshaya.login()