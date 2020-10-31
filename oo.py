"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

(replace this with your answer)


2. What is a class?

A class is a core part of object-oreinted programming. It describes the behavior and state that the object supports. 

3. What is a method?

A method is a action that a object is able to perform. Bascially, a fuction defined on a class.(Always has atleast one parameter, "self")


4. What is an instance in object orientation?

An instance is an ocurrence of any object, existing usually during the runtime of a computer program.('__init__' is called when an instance is created. )


5. How is a class attribute different than an instance attribute?
   

The class attribute is a piece of data on the class itself, rather an instance attribute is set on the object.

"""2. Road Class"""

def__init__(self, speed_limit, lanes):
    self.speed_limit = speed_limit
    self.lanes = lanes 
    


"""3. Update Password"""


class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password

     def updated_password(self, current_password, update_password):
        if self.password == updated_password:
            self.password == update_password;
            else:
            print("wrong password") 


class Library(object): 

    books = []

    def add_textbook(self, title, author):
        title = book(title, author)
        self.books.append(title)

    def find_book(self, author):
        author_of_book = []
        for book in self.books:
            if author == author:
                author_of_book.append(book)
            return author_of_book


class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author


"""5. Rectangle"""


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width
