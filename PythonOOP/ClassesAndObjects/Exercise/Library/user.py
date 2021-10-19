class User:
    def __init__(self,user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if author in library.books_available and book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            if self.username not in library.rented_books:
                library.rented_books[self.username] = {}
            library.rented_books[self.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        days_remaining_to_get_the_book = [days for u in library.rented_books
                                          for book, days in library.rented_books[u].items() if book == book_name]
        if days_remaining_to_get_the_book:
            days_remaining_to_get_the_book = days_remaining_to_get_the_book[0]
            return f'The book "{book_name}" is already rented ' \
                   f'and will be available in {days_remaining_to_get_the_book} days!'

    def return_book(self, author:str, book_name:str, library):
        if book_name in self.books:
            self.books.remove(book_name)
            if author not in library.books_available:
                library.books_available[author] = []
            library.books_available[author].append(book_name)
            library.rented_books[self.username].pop(book_name)
            if library.rented_books[self.username] == {}:
                del library.rented_books[self.username]
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ', '.join(sorted(self.books))
