tests/test_media_item.py
tests/test_movies.py
tests/test_collection.py
tests/test_polymorphism.py
import pytest
from media_item import MediaItem
from movie import Movie

def test_media_item_is_abstract():
    # Cannot instantiate abstract class
    with pytest.raises(TypeError):
        MediaItem("Title", "Genre")

def test_movie_is_subclass_of_mediaitem():
    m = Movie("Iron Man", "Action", ["Robert Downey Jr."])
    assert isinstance(m, MediaItem)
from movie import Movie
from series import Series
from documentary import Documentary

def test_movie_creation():
    m = Movie("Iron Man", "Action", ["Robert Downey Jr."])
    assert m.title == "Iron Man"
    assert m.genre == "Action"

def test_series_creation():
    s = Series("Breaking Bad", "Crime Drama", 5)
    assert s.seasons == 5
    assert "Breaking Bad" in str(s)

def test_documentary_creation():
    d = Documentary("Planet Earth", "Nature", "Earth")
    assert "Nature" in d.topic
from movie_collection import MovieCollection
from movie import Movie

def test_add_item_to_collection():
    collection = MovieCollection()
    m = Movie("Interstellar", "Sci-Fi", ["Matthew McConaughey"])
    collection.add_item(m)
    assert collection.total_items() == 1

def test_remove_item_from_collection():
    collection = MovieCollection()
    m = Movie("Sherlock Holmes", "Mystery", ["Robert Downey Jr."])
    collection.add_item(m)
    collection.remove_item("Sherlock Holmes")
    assert collection.total_items() == 0
from movie_collection import MovieCollection
from movie import Movie
from series import Series
from documentary import Documentary

def test_polymorphic_search():
    collection = MovieCollection()

    m = Movie("Iron Man", "Action", ["Robert Downey Jr."])
    s = Series("Breaking Bad", "Crime Drama", 5)
    d = Documentary("Planet Earth", "Nature", "Nature")

    collection.add_item(m)
    collection.add_item(s)
    collection.add_item(d)

    results = collection.search("Nature")
    assert any(isinstance(item, Documentary) for item in results)
