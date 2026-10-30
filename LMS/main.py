from book import Book, Library
from user import Student, Teacher
from exceptions import OutOfLimitError, NoAvailableCopiesError, BookNotFoundError


book1 = Book(101, "Python", 500, "Priyanshu", 5)
book2 = Book(102, "Java", 600, "Rishi", 3)
book3 = Book(103, "C++", 700, "Rohit", 0)
book4 = Book(104, "C", 800, "Mani", 2)
book5 = Book(105, "JavaScript", 900, "Rohit", 1)
book6 = Book(106, "HTML", 1000, "Rishi", 4)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)


teacher1 = Teacher("Priyanshu", 22, 101)
teacher2 = Teacher("Rishi", 23, 102)

student1 = Student("Rohit", 24, 201)
student2 = Student("Mani", 25, 202)

try:
    print(book1)
    student1.borrow_book1(book1)
    student1.borrow_book1(book1)
    student1.borrow_book1(book1)
    # student1.borrow_book1(book1)
    print(book1)

    library.search_book("Python")
    library.list_book()


except OutOfLimitError as e:
    print(f"{type(e).__name__} : {e}")

except NoAvailableCopiesError as e:
    print(f"{type(e).__name__} : {e}")

except BookNotFoundError as e:
    print(f"{type(e).__name__} : {e}")