from movie import Movie
from documentary import Documentary
from series import Series
from movie_collection import MovieCollection

def main():
    print("=== Movie Manager App (Project 3 Demo) ===\n")

    # ----------------------------
    # Composition: Create collection
    # ----------------------------
    collection = MovieCollection()

    # ----------------------------
    # Inheritance: Create subclasses
    # ----------------------------
    m1 = Movie("Iron Man", "Action", ["Robert Downey Jr.", "Gwyneth Paltrow"])
    m2 = Movie("Interstellar", "Sci-Fi", ["Matthew McConaughey", "Anne Hathaway"])

    d1 = Documentary("Planet Earth", "Nature", "Earth/Nature")
    d2 = Documentary("The Last Dance", "Sports", "Basketball")

    s1 = Series("Breaking Bad", "Crime Drama", 5)
    s2 = Series("Sherlock", "Mystery", 4)

    # ----------------------------
    # Composition: Add to collection
    # ----------------------------
    print("Adding media items to collection...\n")
    for item in [m1, m2, d1, d2, s1, s2]:
        collection.add_item(item)

    # ----------------------------
    # Polymorphism Demo
    # ----------------------------
    print("\n=== Polymorphic Search: keyword = 'Earth' ===")
    results = collection.search("Earth")
    for r in results:
        print(f"→ {r} (period: {r.calculate_loan_period()} days)")

    print("\n=== Polymorphic Search: keyword = 'Drama' ===")
    results = collection.search("Drama")
    for r in results:
        print(f"→ {r} (period: {r.calculate_loan_period()} days)")

    # ----------------------------
    # List all items
    # ----------------------------
    print("\n=== All Items in Collection ===")
    print(collection)

    # ----------------------------
    # Remove item
    # ----------------------------
    print("\nRemoving 'Sherlock'...")
    removed = collection.remove_item("Sherlock")
    print("Removed!" if removed else "Not found.")

    # Display updated list
    print("\n=== Updated Collection ===")
    print(collection)

if __name__ == "__main__":
    main()


