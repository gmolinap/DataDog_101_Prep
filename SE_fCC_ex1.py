"""
https://www.youtube.com/watch?v=1qw5ITr3k9E&ab_channel=freeCodeCamp.org
 Online cloud reading App
 Kindle-like application
 Help designing the code (actual application)

 We're looking for:
    - Users have a library of books that they can add to or remove from
    - Users can set a book from their libary as active
    - The reading application remembers where a user left off in 
    a given book
    - The reading application only displays a page of text at a time
    in the active book
"""

#1. Questions? & Insights
"""
Do you want me to create a high-level design or a low-level design?
What do you mean by "active book"?
How should we store the user's library of books?

- All book in library 
- Remember the active book
- Remember the last page read
- Display a page in active book


Classses:
  - representing a book
    - id: str/int
    - title: string 
    - pages/content in the book: list of strings (per page)
    - last page: int (index of last page read)
  - representing a library
    - collection of books: dict {id: Book()}  (Do you think the id is robust as pk?)
    - active book: variable correspond to id (instead of having a Boolean) None if no active book
"""

#Define the classes

class Book:
    def __init__(self, id, title, content): #last page doesn't need to be initialized
        self.title = title
        self.content = content #long string of characters
        self.last_page = 0 # initialize to 0

        #self.font_size = 12
        #self.chars_per_page = calculate(font_size)

    
    #so it will be better to initialize the id in the constructor
    def display_page(self):
        return self.content[self.last_page]

    def turn_page(self):
        self.last_page += 1
        return self.display_page() #return the next page
    
class Library:
    def __init__(self):
        self.collection = {}
        self.active_book = None
        self.id_counter = 0 #Hack to be unique
        
    def add_to_colletion(self, title, content):
        new_book = Book(self.id_counter, title, content)
        self.collection[new_book.id] = new_book
        self.id_counter += 1

    def remove_from_collection(self, book_id):
        self.collection.pop(book_id)

    def set_active_book(self, book_id):
        self.active_book = book_id

    def display_page(self):
        self.collection[self.active_book].display_page()
    
    def turn_page(self):
        return self.collection[self.active_book].turn_page()
    

#2. Test the classes
Library = Library()
Library.add_to_colletion("Book1", ["Page1", "Page2", "Page3"])
Library.add_to_colletion("Book2", ["Page1", "Page2", "Page3"])
