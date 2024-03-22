import library_interface as lib


def main():
    library = lib.Library()
    author1 = lib.Author('J.K. Rowling', '31 July 1965')
    author2 = lib.Author('Stephen King', '21 September 1947')
    book1 = lib.Book('Harry Potter', author1, 1997)
    book2 = lib.Book('The Shining', author2, 1977)
    library.add_author(author1)
    library.add_author(author2)
    library.add_book(book1)
    library.add_book(book2)
    library.list_books()
    library.list_authors()
    library.books[0].check_out()
    library.list_books()
    library.books[1].check_out()
    library.list_books()
    library.books[0].check_in()
    library.list_books()
    library.books[1].check_in()
    library.list_books()


if __name__ == '__main__':
    main()
