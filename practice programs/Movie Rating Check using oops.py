class Movie:
    def __init__(self,title,genre,rating):
        self.title=title
        self.genre=genre
        self.rating=rating
    def family_friendly(self):
        return self.rating<13
m1=Movie("Finding Nemo", "Animation", 8)
print(f"Family friendly:",m1.family_friendly())