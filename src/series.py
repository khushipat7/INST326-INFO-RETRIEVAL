from media_item import MediaItem

class Series(MediaItem):
    """
    Represents a TV series with seasons.
    """

    def __init__(self, title, genre, actors, seasons):
        super().__init__(title, genre, actors)

        if not isinstance(seasons, int) or seasons <= 0:
            raise ValueError("Seasons must be a positive integer.")

        self._seasons = seasons

    @property
    def seasons(self):
        return self._seasons

    # -------- Polymorphic Overrides -------- #

    def get_description(self):
        return f"{self._title} ({self._genre}) — TV Series with {self._seasons} seasons."

    def calculate_popularity_score(self):
        return 30 + (self._seasons * 10) + (len(self._actors) * 5)

    def __str__(self):
        return f"{self._title} ({self._genre}) — {self._seasons} seasons"

    def __repr__(self):
        return f"Series(title={self._title!r}, genre={self._genre!r}, actors={self._actors!r}, seasons={self._seasons!r})"
