from media_item import MediaItem

class MovieCollection:
    """
    A collection that stores MediaItem objects (Movie, Series, Documentary).

    Demonstrates composition: MovieCollection HAS-A list of media items.
    """

    def __init__(self):
        self._items = []   # internal list for MediaItem objects

    def add_item(self, item):
        """
        Add a Movie, Series, or Documentary to the collection.

        Args:
            item (MediaItem): A subclass instance of MediaItem.

        Raises:
            TypeError: If item is not a MediaItem subclass.
        """
        if not isinstance(item, MediaItem):
            raise TypeError("Item must be a MediaItem subclass.")
        self._items.append(item)

    def remove_item(self, title):
        """
        Remove the first item matching the given title.

        Args:
            title (str): Title of the media to remove.

        Returns:
            bool: True if removed, False if not found.
        """
        for i, item in enumerate(self._items):
            if item.title.lower() == title.lower():
                del self._items[i]
                return True
        return False

    def search(self, keyword):
        """
        Polymorphic search: calls each MediaItem's matches_keyword().

        Args:
            keyword (str): Keyword to search for.

        Returns:
            list: Items that match the keyword.
        """
        return [item for item in self._items if item.matches_keyword(keyword)]

    def list_all(self):
        """Return a shallow copy of all stored media items."""
        return self._items.copy()

    def total_items(self):
        """Return how many items are in the collection."""
        return len(self._items)

    def __str__(self):
        if not self._items:
            return "No items in the collection."
        return "\n".join(str(item) for item in self._items)

