class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        tempBooks: list[Book] = []
        for selfBook in self.books:
            if selfBook.title != book.title or selfBook.author != book.author:
                tempBooks.append(selfBook)
        self.books = tempBooks

    def search_books(self, search_string: str) -> list[Book]:
        tempBooks: list[Book] = []
        search_string = search_string.lower()
        for selfBook in self.books:
            if search_string in selfBook.title.lower():
                tempBooks.append(selfBook)
        
        return tempBooks

