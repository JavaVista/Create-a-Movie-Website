import webbrowser
# Javi's Stage 3 Submission
class Movie():
    '''This a class that provides a way to store movie info'''
    VALID_RATINGS = ('G', 'PG', 'PG-13', 'R', 'NR') #class variable

    def __init__(self, movie_title,rating, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.VALID_RATINGS = rating
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube



    def show_trailer(self):
        ''' Opens trailer in a web browser'''
        webbrowser.open(self.trailer_youtube_url)

