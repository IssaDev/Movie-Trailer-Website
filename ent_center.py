import media
import fresh_tomatoes

# Create instances of favorite movies
toyStory = media.Movie("Toy Story",
                       "The story of a boy and his toys that come to life",
                       "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc",  # noqa
                       "Tom Hanks, Tim Allen, Don Rickles, Wallace Shawn")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",  # noqa
                     "Zoe Saldana, Sam Worthington, Sigourney Weaver, Stephen Lang")  # noqa

black_panther = media.Movie("The Black Panther",
                            "A prince takes his fathers place to lead the wakandan nation",  # noqa
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU",  # noqa
                            "Chadwick Boseman, Michael B Jordan, Lupita Nyongo, Angela Basset")  # noqa

jumanji = media.Movie("Jumanji",
                      "Four friends find a video game that changes their lives",  # noqa
                      "https://upload.wikimedia.org/wikipedia/en/d/dc/Jumanji_Welcome_to_the_Jungle.png",  # noqa
                      "https://www.youtube.com/watch?v=2QKg5SZ_35I",  # noqa
                      "Dwayne Johnson, Kevin Hart, Jack Black, Karen Gillan, Nick Jonas")  # noqa

movies = [toyStory, avatar, black_panther, jumanji]
fresh_tomatoes.open_movies_page(movies)
# black_panther.show_cast()
