class Book:
    def __init__(self, title, author, category, available=True):
        self.title = title
        self.author = author
        self.category = category
        self.available = available

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

# Create a bookstore
bookstore = Bookstore()

# Add some books
bookstore.add_book(Book("Glimpses of World History", "Jawaharlal Nehru", "Fiction"))
bookstore.add_book(Book("Guide", "R.K.Narayan", "Non-fiction"))
bookstore.add_book(Book("Letter from a father to her Daughter", "Jawaharlal Nehru", "Fiction"))

# Search for books by title
search_title = "Glimpses of World History"
results_by_title = bookstore.search_by_title(search_title)
print(f"Books with '{search_title}' in the title:")
for book in results_by_title:
    print(f"{book.title} by {book.author} ({book.category})")

# Search for books by author
search_author = "Jawaharlal Nehru"
results_by_author = bookstore.search_by_author(search_author)
print(f"\nBooks by '{search_author}':")
for book in results_by_author:
    print(f"{book.title} by {book.author} ({book.category})")
