from abc import ABC, abstractmethod

class MediaItem(ABC):
    """Abstract base class for any media (movie, series, documentary)."""

    def __init__(self, title, genre, actors):
        # You keep the SAME validation your Movie class uses
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(genre, str) or not genre.strip():
            raise ValueError("Genre must be a non-empty string.")
        if not isinstance(actors, list) or not all(isinstance(a, str) for a in actors):
            raise ValueError("Actors must be a list of strings.")

        self._title = title.strip().title()
        self._genre = genre.strip().title()
        self._actors = [a.strip() for a in actors]

    @property
    def title(self):
        return self._title

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, new_genre):
        if not isinstance(new_genre, str) or not new_genre.strip():
            raise ValueError("Genre must be a non-empty string.")
        self._genre = new_genre.strip().title()

    @property
    def actors(self):
        return self._actors

    @abstractmethod
    def get_description(self):
        """Return a description string (polymorphic)."""
        pass

    @abstractmethod
    def calculate_popularity_score(self):
        """Return a numeric popularity score."""
        pass
