class Movie:
    """
    Represents a single movie in the collection.

    Attributes:
        title (str): The movie title.
        genre (str): The genre of the movie.
        actors (list): A list of actors in the movie.

    Example:
        >>> m = Movie("Iron Man", "Action", ["Robert Downey Jr.", "Gwyneth Paltrow"])
        >>> print(m)
        Iron Man (Action) starring Robert Downey Jr., Gwyneth Paltrow
    """

    def __init__(self, title, genre, actors):
        """
        Initialize a Movie object with validation.

        Args:
            title (str): The movie title.
            genre (str): The genre (e.g., 'Action', 'Drama').
            actors (list[str]): A list of actor names.

        Raises:
            ValueError: If any argument is invalid or empty.
        """
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(genre, str) or not genre.strip():
            raise ValueError("Genre must be a non-empty string.")
        if not isinstance(actors, list) or not all(isinstance(a, str) for a in actors):
            raise ValueError("Actors must be a list of strings.")

        self._title = title.strip().title()
        self._genre = genre.strip().title()
        self._actors = [a.strip() for a in actors]

    # -------------------
    # Properties
    # -------------------
    @property
    def title(self):
        """str: Get the movie title."""
        return self._title

    @property
    def genre(self):
        """str: Get or set the movie genre."""
        return self._genre

    @genre.setter
    def genre(self, new_genre):
        if not isinstance(new_genre, str) or not new_genre.strip():
            raise ValueError("Genre must be a non-empty string.")
        self._genre = new_genre.strip().title()

    @property
    def actors(self):
        """list: Get the list of actors."""
        return self._actors

    # -------------------
    # Methods
    # -------------------
    def has_actor(self, actor_name):
        """
        Check if an actor is in this movie.

        Args:
            actor_name (str): The actor to search for.

        Returns:
            bool: True if the actor appears, False otherwise.
        """
        return any(actor_name.lower() in a.lower() for a in self._actors)

    def matches_keyword(self, keyword):
        """
        Check if a keyword matches the title or genre.

        Args:
            keyword (str): Keyword to search.

        Returns:
            bool: True if keyword appears in title or genre.
        """
        keyword = keyword.lower()
        return keyword in self._title.lower() or keyword in self._genre.lower()

    def update_genre(self, new_genre):
        """
        Update the genre of the movie.

        Args:
            new_genre (str): The new genre name.
        """
        self.genre = new_genre  # uses setter validation

    # -------------------
    # Representation
    # -------------------
    def __str__(self):
        return f"{self._title} ({self._genre}) starring {', '.join(self._actors)}"

    def __repr__(self):
        return f"Movie(title={self._title!r}, genre={self._genre!r}, actors={self._actors!r})"

