from exceptions import BookNotFoundError

class Book:
    def __init__(self, book_id, title, price, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.price = price
        self.author = author
        self.available_copies = available_copies

    def __str__(self):
        return f"Book id is {self.book_id}, Title is {self.title}, Price is {self.price}, Author name is {self.author} and Available copies is {self.available_copies}" 


class Library :
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for book1 in self.books:
            if book.book_id == book1.book_id:
                book1.available_copies = book1.available_copies + book.available_copies
                break
        else:
            self.books.append(book)


    def delete_book(self, book):
        for book1 in self.books:
            if book.book_id == book1.book_id:
                self.books.remove(book1)
                print("Book deleted successfully...")
                break
        else:
            raise BookNotFoundError("Bood not available...")

    def search_book(self, title):
        for book1 in self.books:
            if book1.title == title:
                print(book1)
                break

        else:
            raise BookNotFoundError("Book is not available...")

    def list_book(self):
        for book1 in self.books:
            print(book1)

        else:
            print(f"Total number of books are : {len(self.books)}")