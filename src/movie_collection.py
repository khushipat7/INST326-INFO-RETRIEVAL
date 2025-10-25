from movie import Movie
from actor import Actor

class MovieCollection:
    """
    Represents a collection of movies and provides methods to manage them.

    Attributes:
        movies (list): A list of Movie objects stored in the collection.
    """ 

    def __init__(self):
        """Initialize an empty movie collection."""
        self._movies = []

    # -------------------
    # Core Methods
    # -------------------
    def add_movie(self, movie):
        """
        Add a Movie object to the collection.

        Args:
            movie (Movie): The movie to add.

        Raises:
            TypeError: If the argument is not a Movie object.
        """
        if not isinstance(movie, Movie):
            raise TypeError("Only Movie objects can be added to the collection.")

        if not self.has_movie(movie.title):
            self._movies.append(movie)

    def remove_movie(self, title):
        """
        Remove a movie from the collection by title.

        Args:
            title (str): The title of the movie to remove.

        Returns:
            bool: True if removed, False if not found.
        """
        formatted = title.strip().title()
        for m in self._movies:
            if m.title == formatted:
                self._movies.remove(m)
                return True
        return False

    def has_movie(self, title):
        """
        Check if a movie exists in the collection.

        Args:
            title (str): Movie title to check.

        Returns:
            bool: True if found, False otherwise.
        """
        return any(m.title == title.strip().title() for m in self._movies)

    def get_movie(self, title):
        """
        Retrieve a Movie object by title.

        Args:
            title (str): Movie title to search for.

        Returns:
            Movie or None: The found Movie object, or None if not found.
        """
        formatted = title.strip().title()
        for m in self._movies:
            if m.title == formatted:
                return m
        return None

    def total_movies(self):
        """Return the total number of movies in the collection."""
        return len(self._movies)

    # -------------------
    # Search & Filtering
    # -------------------
    def search_by_genre(self, genre):
        """
        Search for movies matching a specific genre.

        Args:
            genre (str): The genre to search for.

        Returns:
            list: List of Movie objects that match the genre.
        """
        return [m for m in self._movies if m.genre.lower() == genre.strip().lower()]

    def search_by_actor(self, actor_name):
        """
        Search for all movies featuring a given actor.

        Args:
            actor_name (str): Actor’s name.

        Returns:
            list: List of Movie objects that include the actor.
        """
        formatted = actor_name.strip().title()
        return [m for m in self._movies if formatted in [a.name for a in m.actors]]

    # -------------------
    # Reporting & Summary
    # -------------------
    def summarize(self):
        """
        Return a formatted summary of all movies in the collection.

        Returns:
            str: Summary with movie count and details.
        """
        if not self._movies:
            return "No movies in collection."

        summary_lines = [f"Total Movies: {len(self._movies)}", "-" * 30]
        for m in self._movies:
            summary_lines.append(f"{m.title} ({m.year}) — {m.genre}")
        return "\n".join(summary_lines)

    def get_all_movies(self):
        """Return a list of all Movie objects."""
        return list(self._movies)

    # -------------------
    # Representation
    # -------------------
    def __str__(self):
        return f"MovieCollection with {len(self._movies)} movies."

    def __repr__(self):
        return f"MovieCollection(movies={[m.title for m in self._movies]!r})"

