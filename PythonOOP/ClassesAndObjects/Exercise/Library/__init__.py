from project.library import Library
from project.user import User

user = User(12, 'Peter')
library = Library()
library.add_user(user)

library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})


print(library.books_available)
print(library.rented_books)
print(user.books)

print(user.return_book('J.K.Rowling', 'The Goblet of Fire', library))
user.get_book('J.K.Rowling', 'The Goblet of Fire', 17, library)
user.return_book('J.K.Rowling', 'The Goblet of Fire', library)
user.get_book('J.K.Rowling', 'The Goblet of Fire', 17, library)
print(library.books_available)
print(library.rented_books)
print(user.books)
user.return_book('J.K.Rowling', 'The Goblet of Fire', library)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(user)