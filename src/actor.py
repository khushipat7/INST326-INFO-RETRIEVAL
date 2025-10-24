class Actor:
    """
    Represents an actor and their associated filmography.

    Attributes:
        name (str): The actor's full name.
        movies (list): A list of movie titles the actor appears in.

    Example:
        >>> a = Actor("Robert Downey Jr.")
        >>> a.add_movie("Iron Man")
        >>> a.add_movie("Avengers: Endgame")
        >>> print(a)
        Robert Downey Jr. — 2 movies
    """

    def __init__(self, name):
        """
        Initialize an Actor object.

        Args:
            name (str): The actor’s name.

        Raises:
            ValueError: If name is invalid.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Actor name must be a non-empty string.")

        self._name = name.strip().title()
        self._movies = []

    # -------------------
    # Properties
    # -------------------
    @property
    def name(self):
        """str: The actor's full name (read-only)."""
        return self._name

    @property
    def movies(self):
        """list: Return the list of movies this actor appears in."""
        return list(self._movies)

    # -------------------
    # Methods
    # -------------------
    def add_movie(self, movie_title):
        """
        Add a movie to the actor’s filmography.

        Args:
            movie_title (str): The title of the movie to add.
        """
        if not isinstance(movie_title, str) or not movie_title.strip():
            raise ValueError("Movie title must be a non-empty string.")

        formatted = movie_title.strip().title()
        if formatted not in self._movies:
            self._movies.append(formatted)

    def has_movie(self, movie_title):
        """
        Check if the actor has appeared in a specific movie.

        Args:
            movie_title (str): The movie to check.

        Returns:
            bool: True if the actor has appeared in it, else False.
        """
        return movie_title.strip().title() in self._movies

    def get_filmography(self):
        """
        Return the actor’s filmography as a formatted string.

        Returns:
            str: Comma-separated list of movies or 'No movies listed'.
        """
        if not self._movies:
            return "No movies listed"
        return ", ".join(self._movies)

    def total_movies(self):
        """
        Get the total number of movies the actor appears in.

        Returns:
            int: Count of movies.
        """
        return len(self._movies)

    # -------------------
    # Representation
    # -------------------
    def __str__(self):
        count = len(self._movies)
        plural = "movie" if count == 1 else "movies"
        return f"{self._name} — {count} {plural}"

    def __repr__(self):
        return f"Actor(name={self._name!r}, movies={self._movies!r})"

