from abc import ABC, abstractmethod

class MediaItem(ABC):
    """ Abstract base class for all media types."""

    def __init__(self, title, year, genre, actors=None):
        self.title = title
        self.year = year
        self.genre = genre
        self.actors = actors if actors else []

    @abstractmethod
    def get_description(self):
        """Return a string describing the media item."""
        pass

    @abstractmethod
    def calculate_popularity_score(self):
        """Return a number representing popularity."""
        pass
