class Hotstar:
    def __init__(self,username,pwd):
        self.username=username
        self._pwd=pwd
        print(f"Hello {self.username}.You have successfully logged in")
    def content_access(self):
        print("Welcome to Disney Hotstar \n Limited content")
    def ads(self):
        print("Ads........are runningg")
    def videoqua(self):
        print("Video is playing in 720p")
    def livesports(self):
        print("You dont have access to live sports")
    def download(self):
        print("You dont have access to download")
    def logins(self):
        print("You can login in single device at a time")

class Premium(Hotstar):
    def __init__(self,username,pwd):
        self.username=username
        self.__pwd=pwd
        print(f"Hello {self.username}.You have successfully logged in")
    def content_access(self):
        print("Welcome to Disney Hotstar \n Full content")
    def ads(self):
        print("No Ads")
    def videoqua(self):
        print("Video is playing in 4k")
    def livesports(self):
        print("You have access to live sports")
    def download(self):
        print("You  have access to download")
    def logins(self):
        print("You can login in multiple devices at a time")
    
bhavani=Hotstar("bhavani","bhavani123")
bhavani.content_access()
bhavani.ads()
bhavani.videoqua()
bhavani.livesports()
bhavani.download()
bhavani.logins()

akshaya=Premium("akshaya","akshaya123")
akshaya.content_access()
akshaya.ads()
akshaya.videoqua()
akshaya.livesports()
akshaya.download()
akshaya.logins()