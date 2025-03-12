#decorator
def my_decorator(func):
    def wrapper():
        print("hi dear")
        func()
        print("how are you?")
    return wrapper
@my_decorator
def say_hello():
    print("Hello, World!")

# decorated function
say_hello()

# Base class: Book
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False  

    def display_info(self):
        """Displays book details."""
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"Book ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Status: {status}")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  

    def add_book(self, book):
        """Adds a book to the library."""
        self.books.append(book)
        print(f'Book "{book.title}" added to {self.name} library.')

    def show_books(self):
        """Displays all books in the library."""
        print(f"\n Books available in {self.name} Library:")
        for book in self.books:
            book.display_info()

    def borrow_book(self, book_id):
        """Allows a user to borrow a book."""
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f' You have borrowed "{book.title}". Enjoy reading!')
                else:
                    print(f' Sorry, "{book.title}" is already borrowed.')
                return
        print(" Book ID not found.")

    def return_book(self, book_id):
        """Allows a user to return a book."""
        for book in self.books:
            if book.book_id == book_id:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f'You have returned "{book.title}". Thank you!')
                else:
                    print(f'"{book.title}" was not borrowed.')
                return
        print(" Book ID not found.")

# Main Execution
if __name__ == "__main__":
    # Creating a library
    my_library = Library("Central Library")

    
    book1 = Book("The Alchemist", "Paulo Coelho", 101)
    book2 = Book("Harry Potter", "J.K. Rowling", 102)
    book3 = Book("Atomic Habits", "James Clear", 103)
    book4 = Book("Experiments of Truth","Mahadev Desai",104)

    
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.add_book(book4)

    
    my_library.show_books()

   
    my_library.borrow_book(102)

    
    my_library.show_books()

   
    # my_library.return_book()

    
    my_library.show_books()

# inheritence
class animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

class mammle(animal):
    # def eat(self):
    #     print("eat")
    
    def walk(self):
        print("walk")

# concept of DRY-dont repeat yourself
# inheritence - its a mechanism that allows us to define common behavior or function in one class than inherit it in other class.
class fish(animal):
    # def eat(self):
    #     print("eat")
    
    def swim(self):
        print("swim")
# animal: parent
# mammle: child
m = mammle()
m.eat()
print(m.age)    