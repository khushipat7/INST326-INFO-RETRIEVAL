🎬 Movie Management System — Project 3
INST326: Object-Oriented Programming for Information Science
Advanced OOP with Inheritance, Polymorphism & Composition
Project Overview

The Movie Management System applies advanced object-oriented programming concepts to model movies, movie categories, media containers, and a system for managing them.

The current project demonstrates:
Abstract base classes
Inheritance hierarchies
Polymorphic method behavior
Composition relationships between objects
System-level integration and testing
This system mimics a real-world movie library, allowing users to store movies, organize them into containers such as watchlists and favorites, and apply different behaviors depending on movie type.

System Architecture

The system contains two inheritance hierarchies and one composition system, modeled after the Garden sample.

Inheritance Hierarchies
Movie Hierarchy
AbstractMovie (ABC)
├── Movie (base implementation)
│   ├── ActionMovie
│   ├── ComedyMovie
│   └── DocumentaryMovie


AbstractMovie enforces core movie requirements:
get_rating()
get_category()
get_watch_time()
Each child class provides polymorphic behavior such as:

Different rating systems

Runtime adjustments

Category identification

Media Container Hierarchy
AbstractMediaContainer (ABC)
└── MediaContainer (base)
    ├── Watchlist
    ├── Favorites
    └── HistoryList


Each container:
Stores multiple movies (composition)
Implements methods required by the ABC:
add_movie()
remove_movie()
get_total_runtime()

Composition Relationships
MovieManager

The MovieManager ties everything together:

Has many movies
Has many containers
Provides search, summary, and management functionality

📁 MediaContainer

Each container has movies, but is not a movie.
This demonstrates proper has-a (composition) rather than is-a (inheritance).


Polymorphism

Different movie types override behaviors:
ActionMovie increases runtime (e.g., action scenes)
DocumentaryMovie decreases runtime (tighter editing)
ComedyMovie uses neutral runtime
Ratings vary by movie type

Abstract Base Classes
Using Python’s abc module ensures:
You cannot instantiate abstract classes
All child classes must implement required methods
A consistent interface for all movie types and container

Composition

MovieManager manages:
A collection of all movies
A collection of media containers
Cross-object lookups
Containers each store their own list of movies.

Encapsulation & Validation

No external dependencies required.

Running the System
Run Demo
python3 demo.py


This demonstrates:

Instantiating movie objects, Area-based polymorphism
, Adding/removing movies from containers

Run Testing method has been demonstrated:
python3 -m unittest test_movie_system.py -v


Tests cover:

Inheritance

Abstract class enforcement

Polymorphism

Composition

Integration of all features

Usage Examples
Creating Movies
from movies import ActionMovie, ComedyMovie, DocumentaryMovie

m1 = ActionMovie("m1", "John Wick", "Action", 110)
m2 = ComedyMovie("m2", "Ted", "Comedy", 95)
m3 = DocumentaryMovie("m3", "Oceans", "Documentary", 85)

Using Media Containers
from libraries import Watchlist, Favorites

wl = Watchlist("w1", "Weekend Watchlist")
wl.add_movie(m1)
wl.add_movie(m2)

Using MovieManager
from movie_manager import MovieManager

manager = MovieManager("My Movies")

manager.add_movie(m1)
manager.add_movie(m2)
manager.add_container(wl)

summary = manager.get_system_summary()
print(summary)

📂 File Structure
movie_system/
├── base_classes.py        # Abstract classes
├── movies.py              # Movie classes + polymorphism
├── libraries.py           # Media container classes
├── movie_manager.py       # Composition manager
├── test_movie_system.py   # Unit tests
└── demo.py                # Demonstration script

📝 Design Decisions
Why Inheritance?

Movies share attributes (title, runtime, category) but differ in behavior (runtime adjustment, rating).
Containers share structure but represent different organizational types.

Why Abstract Classes?

They enforce required methods:

Every Movie must define rating, category, and watch time

Every Container must define add/remove runtime calculation

Why Composition?

A movie is not a container.
A container is not a manager.
They simply contain each other.

Composition ensures loose coupling and scalable design.
 
🙋 Team Information

Student: Muhammad, Khushi, Dritesh, Ben 
Section: 0303
Completion Date: November 23rd 2025

