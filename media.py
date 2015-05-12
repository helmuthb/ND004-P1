class Movie:
    """
    Class for holding a single movie.
    A Movie has a title (string describing the movie),
    a poster_image_url (a URL pointing to a poster image),
    and a trailer_youtube_url (a URL pointing to the
    youtube trailer video).
    """
    
    def __init__(self, title, story_line, poster_image_url,
                 trailer_youtube_url, actors, release_date):
        # copy arguments into fields of the same name in the object.
        # The initializer function can be called with positional as
        # well as named arguments - for readibility the later form is
        # preferred.
        self.title               = title
        self.story_line          = story_line
        self.poster_image_url    = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.actors              = actors
        self.release_date        = release_date
