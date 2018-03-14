import webbrowser
class Movie():
    def __init__(self, movie_title, movie_storyline,poster_image, youtube_trailer, cast):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer = youtube_trailer
        self.cast = cast

    def show_trailer(self):
        webbrowser.open(self.trailer)
    
    def show_image(self):
        webbrowser.open(self.poster_image_url)

    def show_cast(self):
        print(self.cast)