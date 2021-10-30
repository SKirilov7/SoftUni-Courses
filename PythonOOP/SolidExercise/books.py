class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        try:
            return [book for book in self.books if book.title == title][0]
        except IndexError:
            return 'Book not found in our library'


class PageTurnerMixin:
    def turn_page(self, page):
        self.page = page


class Book(PageTurnerMixin):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def __repr__(self):
        return f'This "{self.title}" from the author-{self.author}.'


a = Library()
book = Book('sasda', 'asd')
a.add_book(book)
print(a.find_book('sasda'))
