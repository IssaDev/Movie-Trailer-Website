import webbrowser


class Movie():
    """creates an instance to build a list of movies each differing from the other.

      Attributes:
      title (str): The title of the movie.
      storyline(str): Quick plot of the movie.
      poster_image_url(url): Link to the poster image for the movie.
      youtube_trailer(url): Link to the official movie trailer on youtube.
      cast(str): List of the main cast.

      """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 youtube_trailer, cast):
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
