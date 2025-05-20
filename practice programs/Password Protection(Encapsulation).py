class Password:
    def __init__(self,password):
        self.__password=password
    def change_password(self,old,new):
        if old==self.__password:
            self.__password=new
            print("Password changed:",{self.__password})
        else:
            print("Incorrect old password")
p=Password("alex23")
p.change_password("alex23","alex@123")
