"""All methods used to get site data"""

from .user import UserMethods
from .artist import ArtistMethods
from .album import AlbumMethods
from .genre import GenreMethods


class AOTY(UserMethods, ArtistMethods, AlbumMethods, GenreMethods):
    """A light weight python library that acts as an API for https://www.albumoftheyear.org"""

    def __init__(self, user_agent="Mozilla/5.0", **kwargs):
        """Initializes the required variables for getting website data.
        Required for easier caching
        """
        super().__init__(user_agent=user_agent, **kwargs)
