# Practicing classes

class movie:
    def title(self, movie):
        self.movie_title = movie
        return f"The movie is called {self.movie_title}"

    def duration(self, x):
        self.showtime = x
        return f"The movie is {self.showtime}hrs long"

entertainment = movie()

print(entertainment.title("Transformers"))
print(entertainment.duration(2))
