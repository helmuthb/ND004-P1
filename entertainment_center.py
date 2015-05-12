import media
from fresh_tomatoes import open_movies_page

# function for creating a list of Movies
def get_movie_list():
    # creating an empty list which will be filled with entries
    movie_list = []
    # create a Movie object and append it to the list
    movie_list.append(media.Movie(
        title="Paper Towns",
        story_line="Paper Towns is an upcoming American teen romantic "
            "mystery film, directed by Jake Schreier based on "
            "the 2008 novel of the same name by John Green.",
        poster_image_url="http://img09.deviantart.net/cbf5/i/2015/073"
            "/a/3/paper_towns__movie_poster__by_blantonl98-d8loztt.jpg",
        trailer_youtube_url="https://youtube.com/watch?v=rFGiHm5WMLk",
        actors=["Nat Wolff", "Cara Delevingne"],
        release_date="2015"))
    # create another Movie object and append it to the list
    movie_list.append(media.Movie(
        title="Lucifer",
        story_line="Lucifer is an upcoming American television series "
            "that is set to air on Fox.",
        poster_image_url="http://www.joblo.com/images_arrownews/"
            "lucifer-title.jpg",
        trailer_youtube_url="https://youtube.com/watch?v=X4bF_quwNtw",
        actors=["Tom Ellis", "Lesley-Ann Brandt", "Lauren German"],
        release_date="2015"))
    # return the compiled list of Movie objects
    return movie_list

# get movie list
movies = get_movie_list()
# create the HTML page and open it
open_movies_page(movies)
