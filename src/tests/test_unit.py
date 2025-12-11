import pytest
import builtins
from types import SimpleNamespace

# Skip entire file gracefully if core modules are missing
FunctionLibrary = pytest.importorskip("FunctionLibrary")
Actor = pytest.importorskip("actor").Actor
media_item = pytest.importorskip("media_item")
Movie = pytest.importorskip("movie").Movie
Series = pytest.importorskip("series").Series

# ---------- Unit tests for FunctionLibrary ----------
def test_format_movie_title_and_validate():
    assert FunctionLibrary.format_movie_title("  the matrix ") == "The Matrix"
    assert FunctionLibrary.format_movie_title(123) is None

    good = {"title": "A", "genre": "G", "actors": ["X"]}
    bad = "not a dict"
    assert FunctionLibrary.validate_movie_data(good) is True
    assert FunctionLibrary.validate_movie_data(bad) is False

def test_add_and_count_and_remove_movie(capfd):
    coll = []
    ok = FunctionLibrary.add_movie(coll, "Inception", "Sci-Fi", ["Leonardo DiCaprio"])
    assert ok is True
    assert FunctionLibrary.count_total_movies(coll) == 1

    # remove case-insensitive
    assert FunctionLibrary.remove_movie(coll, "INCEPTION") is True
    assert FunctionLibrary.count_total_movies(coll) == 0

def test_search_by_actor_and_keyword():
    coll = []
    FunctionLibrary.add_movie(coll, "The Notebook", "Romance", ["Ryan Gosling", "Rachel McAdams"])
    matches = FunctionLibrary.search_by_actor(coll, "ryan")
    assert "The Notebook" in matches

    kw = FunctionLibrary.search_by_keyword(coll, "rom")
    assert "The Notebook" in kw

def test_build_index_and_find_similar_movies():
    coll = []
    FunctionLibrary.add_movie(coll, "A", "Action", ["X", "Y"])
    FunctionLibrary.add_movie(coll, "B", "Action", ["X", "Z"])
    index = FunctionLibrary.build_keyword_index(coll)
    assert "action" in index
    sims = FunctionLibrary.find_similar_movies(coll, "A")
    assert any(title == "B" for title, score in sims)

def test_generate_collection_report_structure(capfd):
    coll = []
    FunctionLibrary.add_movie(coll, "Blade Runner", "Sci-Fi", ["Harrison Ford"])
    report = FunctionLibrary.generate_collection_report(coll)
    assert isinstance(report, dict)
    assert report["total_movies"] == 1
    assert "Sci-Fi" in report["genre_frequency"] or "Sci-Fi/Noir" in report["genre_frequency"]

# ---------- Unit tests for Actor ----------
def test_actor_basic_behavior():
    a = Actor("robert downey jr.")
    assert a.name == "Robert Downey Jr."
    assert a.total_movies() == 0
    assert a.get_filmography() == "No movies listed"

    a.add_movie("Iron Man")
    assert a.has_movie("iron man")
    assert a.total_movies() == 1
    assert "Iron Man" in a.get_filmography()
    assert "movie" in str(a)  # "1 movie" or "movies"

def test_actor_invalid_init_and_add():
    with pytest.raises(ValueError):
        Actor("")  # empty
    a = Actor("Test Actor")
    with pytest.raises(ValueError):
        a.add_movie("")  # invalid title

# ---------- Unit tests for Movie and Series ----------
def test_movie_and_mediaitem_behavior():
    # MediaItem is abstract; instantiating may raise TypeError depending on how it's defined
    with pytest.raises(TypeError):
        # should fail if MediaItem is correctly abstract
        media_item.MediaItem("T", "G", ["A"])

    m = Movie("The Grand Budapest Hotel", "Comedy", ["Ralph Fiennes"], duration=99)
    assert m.title == "The Grand Budapest Hotel"
    assert m.has_actor("Ralph")
    assert m.matches_keyword("grand")
    desc = m.get_description()
    assert "Movie" in desc or "starring" in desc
    assert isinstance(m.calculate_popularity_score(), int)

def test_series_behavior():
    s = Series("Fleabag", "Comedy", ["Phoebe Waller-Bridge"], seasons=2)
    assert s.seasons == 2
    assert "TV Series" in s.get_description() or "Series" in s.get_description()
    assert s.calculate_popularity_score() > 0
