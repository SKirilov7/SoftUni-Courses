from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library('Library')

    def test_if_init_attaches_correctly(self):
        self.assertEqual('Library', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_if_name_is_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            library = Library('')
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_with_non_existing_author(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book('Pesho', "Pesho's history")
        self.assertEqual({'Pesho': ["Pesho's history"]}, self.library.books_by_authors)

    def test_add_book_with_existing_author(self):
        self.library.books_by_authors = {'Pesho': ["Pesho's history"]}
        self.library.add_book('Pesho', 'new book')
        self.assertEqual({'Pesho': ["Pesho's history", 'new book']}, self.library.books_by_authors)

    def test_add_reader_with_non_existing_reader(self):
        self.assertEqual({}, self.library.readers)
        self.library.add_reader('Pesho')
        self.assertEqual({'Pesho': []}, self.library.readers)

    def test_add_reader_with_existing_reader(self):
        self.library.readers = {'Pesho': []}
        return_message = self.library.add_reader('Pesho')
        self.assertEqual("Pesho is already registered in the Library library.", return_message)

    def test_rent_book_with_non_existing_reader(self):
        self.assertEqual({}, self.library.readers)
        result = self.library.rent_book('Pesho', 'Ivan', 'Book')
        self.assertEqual("Pesho is not registered in the Library Library.", result)

    def test_rent_book_with_non_existing_author(self):
        self.library.readers = {'Pesho': []}
        self.assertEqual({}, self.library.books_by_authors)
        result = self.library.rent_book('Pesho', 'Ivan', 'Book')
        self.assertEqual("Library Library does not have any Ivan's books.", result)

    def test_rent_book_with_non_existing_book(self):
        self.library.readers = {'Pesho': []}
        self.library.books_by_authors = {'Ivan': ['book']}
        result = self.library.rent_book('Pesho', 'Ivan', 'Book2')
        self.assertEqual("""Library Library does not have Ivan's "Book2".""", result)

    def test_rent_book_with_everything_existing(self):
        self.library.readers = {'Pesho': []}
        self.library.books_by_authors = {'Ivan': ['book']}
        self.library.rent_book('Pesho', 'Ivan', 'book')
        self.assertEqual({'Pesho': [{'Ivan': 'book'}]}, self.library.readers)
        self.assertEqual({'Ivan': []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
