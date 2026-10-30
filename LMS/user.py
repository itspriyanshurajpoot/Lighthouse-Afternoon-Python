from exceptions import NoAvailableCopiesError, OutOfLimitError

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.borrow_book = []

    def borrow_book1(self, book):
        if book.available_copies > 0 :
            self.borrow_book.append(book)
            book.available_copies = book.available_copies - 1
            print("Book borrowed successfully...")
        else:
            raise NoAvailableCopiesError("Copies are not available...")

    def return_book(self, book):
        for book1 in self.borrow_book:
            if book1.book_id == book.book_id:
                self.borrow_book.remove(book1)
                book.available_copies = book.available_copies + 1
                break
        else:
            raise NoAvailableCopiesError("You didn't borrow that book")

class Teacher(User):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def limit(self):
        return 5

    def borrow_book1(self, book):
        if len(self.borrow_book) < self.limit() :
            super().borrow_book(book)
        else:
            raise OutOfLimitError("Limit reached...")

class Student(User):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def limit(self):
        return 3

    def borrow_book1(self, book):
        if len(self.borrow_book) < self.limit():
            super().borrow_book1(book)
        else:
            raise OutOfLimitError("Limit reached...")