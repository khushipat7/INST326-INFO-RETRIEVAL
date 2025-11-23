from media_item import MediaItem

class Documentary(MediaItem):
    """
    Represents a documentary film or series.
    """

    def __init__(self, title, genre, actors, topic):
        super().__init__(title, genre, actors)

        if not isinstance(topic, str) or not topic.strip():
            raise ValueError("Topic must be a non-empty string.")

        self._topic = topic.strip().title()

    @property
    def topic(self):
        return self._topic

    # -------- Polymorphic Overrides -------- #

    def get_description(self):
        return f"{self._title} ({self._genre}) — Documentary on {self._topic}"

    def calculate_popularity_score(self):
        return 40 + len(self._topic) + (len(self._actors) * 3)

    def __str__(self):
        return f"{self._title} — Documentary about {self._topic}"

    def __repr__(self):
        return f"Documentary(title={self._title!r}, topic={self._topic!r})"
