from collections import Counter

class Report:
    """
    Represents a summary report for a MovieCollection.

    This class analyzes a collection of movies and produces
    insights such as genre frequency, most common actors,
    and overall statistics.

    Example:
        report = Report(collection)
        print(report.generate_summary())
    """

    def __init__(self, movie_collection):
        """
        Initialize a report for the given MovieCollection.

        Args:
            movie_collection (MovieCollection): The collection to analyze.

        Raises:
            TypeError: If movie_collection is not a MovieCollection.
        """
        from movie_collection import MovieCollection
        if not isinstance(movie_collection, MovieCollection):
            raise TypeError("Expected a MovieCollection instance.")
        self._collection = movie_collection

    # -------------------
    # Analytics Methods
    # -------------------
    def total_movies(self):
        """Return the total number of movies in the collection."""
        return self._collection.total_movies()

    def genre_frequency(self):
        """Return a dictionary counting how many movies per genre."""
        genres = [movie.genre for movie in self._collection.movies]
        return dict(Counter(genres))

    def actor_appearances(self):
        """Return a dictionary of actor names and their appearance counts."""
        actors = []
        for movie in self._collection.movies:
            actors.extend([actor.name for actor in movie.actors])
        return dict(Counter(actors))

    def most_popular_actor(self):
        """Return the actor who appears in the most movies."""
        appearances = self.actor_appearances()
        if not appearances:
            return None
        return max(appearances, key=appearances.get)

    # -------------------
    # Reporting
    # -------------------
    def generate_summary(self):
        """
        Generate a textual report summarizing the collection.

        Returns:
            str: A formatted string report.
        """
        total = self.total_movies()
        genre_data = self.genre_frequency()
        actor_data = self.actor_appearances()

        report_lines = [
            f"=== Movie Collection Report ===",
            f"Total Movies: {total}",
            "\nGenre Frequency:"
        ]
        for genre, count in genre_data.items():
            report_lines.append(f"  - {genre}: {count}")

        report_lines.append("\nActor Appearances:")
        for actor, count in sorted(actor_data.items(), key=lambda x: x[1], reverse=True):
            report_lines.append(f"  - {actor}: {count} appearance(s)")

        most_popular = self.most_popular_actor()
        if most_popular:
            report_lines.append(f"\nMost Popular Actor: {most_popular}")

        return "\n".join(report_lines)

    # -------------------
    # Representations
    # -------------------
    def __str__(self):
        return f"Report for {self.total_movies()} movies."

    def __repr__(self):
        return f"Report(collection_size={self.total_movies()})"

