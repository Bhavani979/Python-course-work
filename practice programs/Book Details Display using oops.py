class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display_info(self):
        print(f"Title:{self.title},Author:{self.author},Price:{self.price}")
book1=Book("Clean code","Robert Martin","450")
book1.display_info()