from movie import Movie
from actor import Actor
from movie_collection import MovieCollection

class MovieManagerApp:
    """
    Main application class for managing a movie collection.

    This class provides a high-level interface for adding, searching,
    and summarizing movies. It integrates all other classes in the system.
    """

    def __init__(self):
        """Initialize the movie manager with an empty MovieCollection."""
        self._collection = MovieCollection()

    # -------------------
    # Movie Management
    # -------------------
    def add_movie(self, title, year, genre):
        """
        Add a new movie to the system.

        Args:
            title (str): The title of the movie.
            year (int): The release year.
            genre (str): The genre category.

        Returns:
            Movie: The created Movie object.
        """
        movie = Movie(title, year, genre)
        self._collection.add_movie(movie)
        return movie

    def remove_movie(self, title):
        """
        Remove a movie by title.

        Args:
            title (str): The title of the movie to remove.

        Returns:
            bool: True if removed, False otherwise.
        """
        return self._collection.remove_movie(title)

    def add_actor_to_movie(self, movie_title, actor_name):
        """
        Add an actor to a specific movie.

        Args:
            movie_title (str): The title of the movie.
            actor_name (str): The actor’s name.

        Raises:
            ValueError: If the movie is not found.
        """
        movie = self._collection.get_movie(movie_title)
        if not movie:
            raise ValueError(f"Movie '{movie_title}' not found in collection.")

        actor = Actor(actor_name)
        movie.add_actor(actor)

    # -------------------
    # Search & Analysis
    # -------------------
    def search_movies_by_genre(self, genre):
        """Return all movies that match the given genre."""
        return self._collection.search_by_genre(genre)

    def search_movies_by_actor(self, actor_name):
        """Return all movies featuring the given actor."""
        return self._collection.search_by_actor(actor_name)

    # -------------------
    # Summary & Display
    # -------------------
    def show_summary(self):
        """Print a summary of all movies in the collection."""
        print(self._collection.summarize())

    def total_movies(self):
        """Return total number of movies managed."""
        return self._collection.total_movies()

    # -------------------
    # Representation
    # -------------------
    def __str__(self):
        return f"MovieManagerApp managing {self.total_movies()} movies."

    def __repr__(self):
        return f"MovieManagerApp(collection={repr(self._collection)})"


# -------------------
# Example Run (for demo_test)
# -------------------
if __name__ == "__main__":
    app = MovieManagerApp()

    # Add movies
    app.add_movie("Iron Man", 2008, "Action")
    app.add_movie("Avengers: Endgame", 2019, "Action")
    app.add_movie("Inception", 2010, "Sci-Fi")

    # Add actors
    app.add_actor_to_movie("Iron Man", "Robert Downey Jr.")
    app.add_actor_to_movie("Avengers: Endgame", "Robert Downey Jr.")
    app.add_actor_to_movie("Avengers: Endgame", "Scarlett Johansson")
    app.add_actor_to_movie("Inception", "Leonardo DiCaprio")

    # Search examples
    print("\nMovies featuring Robert Downey Jr.:")
    for m in app.search_movies_by_actor("Robert Downey Jr."):
        print(" -", m.title)

    print("\nAction movies:")
    for m in app.search_movies_by_genre("Action"):
        print(" -", m.title)

    print("\nFull Summary:")
    app.show_summary()

