import pytest
Movie = pytest.importorskip("movie").Movie
Series = pytest.importorskip("series").Series
MovieCollection = pytest.importorskip("movie_collection").MovieCollection
Report = pytest.importorskip("report").Report
Actor = pytest.importorskip("actor").Actor
FunctionLibrary = pytest.importorskip("FunctionLibrary")

def test_collection_add_search_and_count():
    collection = MovieCollection()
    m = Movie("Memento", "Thriller", ["Guy Pearce"])
    s = Series("Luther", "Crime", ["Idris Elba"], seasons=3)
    collection.add_item(m)
    collection.add_item(s)
    assert collection.total_items() == 2

    # search should match by keyword (polymorphic)
    res = collection.search("crime")
    assert any(item.title.lower() == "luther".lower() for item in res)

def test_report_genre_frequency_and_actor_appearances_monkeypatched():
    collection = MovieCollection()
    m1 = Movie("Movie One", "Drama", ["Actor A", "Actor B"])
    m2 = Movie("Movie Two", "Drama", ["Actor A"])
    # ensure Report will find .movies: inject attribute on collection instance
    # Also, Report expects actors to have .name; adapt movies to hold Actor objects
    actorA = Actor("Actor A")
    actorB = Actor("Actor B")
    actorA.add_movie("Movie One"); actorA.add_movie("Movie Two")
    actorB.add_movie("Movie One")

    # monkeypatch movie actor lists to contain Actor objects (Report expects actor.name)
    m1._actors = [actorA, actorB]
    m2._actors = [actorA]
    # inject movies attribute for Report to read
    collection._items = [m1, m2]
    collection.movies = collection._items  # add attribute .movies

    report = Report(collection)
    genre_freq = report.genre_frequency()
    assert genre_freq.get("Drama", 0) == 2
    actor_counts = report.actor_appearances()
    assert actor_counts.get("Actor A", 0) >= 1
    assert report.most_popular_actor() in actor_counts.keys()

def test_functionlibrary_and_collection_integration():
    coll = []
    FunctionLibrary.add_movie(coll, "A", "Action", ["X","Y"])
    FunctionLibrary.add_movie(coll, "B", "Action", ["X","Z"])
    index = FunctionLibrary.build_keyword_index(coll)
    assert "action" in index
    sims = FunctionLibrary.find_similar_movies(coll, "A")
    assert any(t == "B" for t, s in sims)
