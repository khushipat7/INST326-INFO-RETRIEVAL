from media_item import MediaItem

class Movie(MediaItem):
    """
    Represents a single movie in the collection.
    """

    def __init__(self, title, genre, actors, duration=None):
        super().__init__(title, genre, actors)
        self._duration = duration

    # -------------------
    # Additional Movie Features (You Already Had)
    # -------------------

    def has_actor(self, actor_name):
        return any(actor_name.lower() in a.lower() for a in self._actors)

    def matches_keyword(self, keyword):
        keyword = keyword.lower()
        return keyword in self._title.lower() or keyword in self._genre.lower()

    def update_genre(self, new_genre):
        self.genre = new_genre

    # -------------------
    # POLYMORPHIC METHODS (Project 3 REQUIRED)
    # -------------------

    def get_description(self):
        return f"{self._title} ({self._genre}) — Movie starring {', '.join(self._actors)}"

    def calculate_popularity_score(self):
        base = 50
        actor_bonus = len(self._actors) * 5
        return base + actor_bonus

    # -------------------
    # Representation
    # -------------------

    def __str__(self):
        return f"{self._title} ({self._genre}) starring {', '.join(self._actors)}"

    def __repr__(self):
        return f"Movie(title={self._title!r}, genre={self._genre!r}, actors={self._actors!r})"


