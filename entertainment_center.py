import media
from fresh_tomatoes import open_movies_page

# function for creating a list of Movies
def get_movie_list():
    movie_list = []
    movie_list.append(media.Movie(
        "Paper Towns",
        "Paper Towns is an upcoming American teen romantic mystery film, directed by Jake Schreier based on the 2008 novel of the same name by John Green.",
        "http://img09.deviantart.net/cbf5/i/2015/073/a/3/paper_towns__movie_poster__by_blantonl98-d8loztt.jpg",
        "https://www.youtube.com/watch?v=rFGiHm5WMLk",
        ["Nat Wolff", "Cara Delevingne"],
        2015))
    movie_list.append(media.Movie(
        "Lucifer",
        "Lucifer is an upcoming American television series that is set to air on Fox",
        "http://www.joblo.com/images_arrownews/lucifer-title.jpg",
        "https://www.youtube.com/watch?v=X4bF_quwNtw",
        ["Tom Ellis", "Lesley-Ann Brandt", "Lauren German"],
        2015))
    return movie_list

# get movie list
movies = get_movie_list()
# create the HTML page and open it
open_movies_page(movies)
