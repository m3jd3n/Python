class Author:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth


class Book:
    def __init__(self, title, author, year, status = 'available'):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def is_available(self):
        if self.status == 'available':
            return True
        else:
            return False

    def check_out(self):
        if self.is_available():
            self.status = 'checked out'
        else:
            print('Book is not available')

    def check_in(self):
        if not self.is_available():
            self.status = 'available'
        else:
            print('Book is already available')

class Library:
    def __init__(self):
        self.books = []
        self.authors = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_author(self, author):
        self.authors.append(author)

    def remove_author(self, author):
        self.authors.remove(author)

    def list_books(self):
        for book in self.books:
            print(book.title)

    def list_authors(self):
        for author in self.authors:
            print(author.name)





