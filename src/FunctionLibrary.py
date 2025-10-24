def display_welcome_message():
    """Display a simple welcome message for the program."""
    print("🎬 Welcome to the Movie Manager!")
    print("Track, search, and analyze your favorite films.\n")


def format_movie_title(title):
    """Return a title formatted in title case."""
    if not isinstance(title, str):
        return None
    return title.strip().title()


def validate_movie_data(movie):
    """Check if the movie dictionary has valid structure and data."""
    required_keys = ["title", "genre", "actors"]
    if not isinstance(movie, dict):
        return False
    for key in required_keys:
        if key not in movie or not movie[key]:
            return False
    return True


def add_movie(collection, title, genre, actors):
    """Add a movie to the collection if it’s valid."""
    movie = {"title": format_movie_title(title), "genre": genre, "actors": actors}
    if validate_movie_data(movie):
        collection.append(movie)
        return True
    return False


def list_movies(collection):
    """Print all movies in the collection."""
    if not collection:
        print("No movies in collection yet.")
    else:
        print("\n🎥 Movie Collection:")
        for i, m in enumerate(collection, 1):
            print(f"{i}. {m['title']} — {m['genre']}")


def remove_movie(collection, title):
    """Remove a movie by title (case-insensitive)."""
    title = title.lower().strip()
    for movie in collection:
        if movie["title"].lower() == title:
            collection.remove(movie)
            return True
    return False


def search_by_actor(collection, actor):
    """Return a list of movies featuring the given actor."""
    matches = []
    for movie in collection:
        for name in movie["actors"]:
            if actor.lower() in name.lower():
                matches.append(movie["title"])
    return matches


def search_by_keyword(collection, keyword):
    """Search movies by keyword found in title or genre."""
    keyword = keyword.lower().strip()
    results = []
    for movie in collection:
        if keyword in movie["title"].lower() or keyword in movie["genre"].lower():
            results.append(movie["title"])
    return results


def update_movie_genre(collection, title, new_genre):
    """Update a movie’s genre if the title exists."""
    for movie in collection:
        if movie["title"].lower() == title.lower():
            movie["genre"] = new_genre
            return True
    return False


def count_total_movies(collection):
    """Return the total number of movies."""
    return len(collection)
  

def generate_collection_report(collection):
    """
    Generate a summary report with total movies,
    genre frequency, and actor appearances.
    """
    report = {
        "total_movies": len(collection),
        "genre_frequency": {},
        "actor_count": {}
    }

    for movie in collection:
        genre = movie["genre"]
        report["genre_frequency"][genre] = report["genre_frequency"].get(genre, 0) + 1

        for actor in movie["actors"]:
            report["actor_count"][actor] = report["actor_count"].get(actor, 0) + 1

    print("\n📊 Movie Collection Report:")
    print(f"Total Movies: {report['total_movies']}")
    print("\nGenre Frequency:")
    for g, c in report["genre_frequency"].items():
        print(f"  - {g}: {c}")

    print("\nTop Actors:")
    for a, c in sorted(report["actor_count"].items(), key=lambda x: x[1], reverse=True):
        print(f"  - {a}: {c} appearances")

    return report


def find_similar_movies(collection, movie_title):
    """
    Find similar movies based on shared actors and genre.
    Returns a sorted list of (title, similarity_score) tuples.
    """
    movie_title = movie_title.lower()
    target_movie = next((m for m in collection if m["title"].lower() == movie_title), None)
    if not target_movie:
        return []

    similarities = []
    for movie in collection:
        if movie == target_movie:
            continue
        shared_actors = len(set(movie["actors"]) & set(target_movie["actors"]))
        same_genre = 1 if movie["genre"] == target_movie["genre"] else 0
        score = shared_actors * 2 + same_genre
        if score > 0:
            similarities.append((movie["title"], score))

    return sorted(similarities, key=lambda x: x[1], reverse=True)


def build_keyword_index(collection):
    """
    Build an index mapping keywords (from titles and genres)
    to movie titles where they appear.
    """
    index = {}
    for movie in collection:
        words = (movie["title"] + " " + movie["genre"]).lower().split()
        for word in words:
            if len(word) <= 2:
                continue  # skip small words like "to", "of", etc.
            if word not in index:
                index[word] = []
            index[word].append(movie["title"])

    return index




