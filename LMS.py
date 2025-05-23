import time
import sqlite3

#sqlite 3 is a library that acts as a bridge between sql and python

#conn.close()
dbconnection = sqlite3.connect("library.db",check_same_thread=False)


class Base:
   
    def __init__(self):
      self.conn = dbconnection
      self.cursor = self.conn.cursor()
    def commit(self):
      self.conn.commit()
      


class Library(Base):
  def __init__(self,numbooks,location):
    super().__init__()
    self.numbooks = numbooks
    self.location = location
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS borrowedbooks(
                   id INTEGER PRIMARY KEY,
                   memberid INTEGER,
                   borrowdate DATE,
                   returndate DATE)""")
    self.commit()

  def addbook(self):
    print("What book to do want to add")
    title = input("Title of the book?\n")
    numpages = int(input("Number of pages of the book?\n"))
    author = input("Author of the book?\n")
    # addbooks(title,numpages,author)
    b1 = Book(title,numpages,author)
    print(b1.title,b1.numpages,b1.author)

    
    self.cursor.execute("""CREATE TABLE IF NOT EXISTS books(
      id INTEGER PRIMARY KEY,
      title TEXT,
      numpages INTEGER,
      author TEXT
    )""")

    self.commit()
    


    b1.addbooktodb()

  def deletebook(self,title):
     self.cursor.execute("DELETE from books WHERE title = ?",(title,))
     self.commit()
  #@classmethod
  def viewbooks(self):
    self.cursor.execute("SELECT * FROM books")
    data = self.cursor.fetchall()
    return data 
    #for i in data:
      #print(i)



class Book(Base):
  def __init__(self,title,numpages,author):
    super().__init__()
    self.title = title
    self.numpages = numpages
    self.author = author

  def addbooktodb(self):
    self.cursor.execute("""
    INSERT INTO books (title,numpages,author)
    VALUES (?,?,?)

    """,(self.title,self.numpages,self.author))
    self.commit()
    print("Book added successfully")



  def read(self):
    print("You are reading: "+self.title+"by"+self.author)
    with open("hpatgof.txt") as file:
      lines = file.readlines()
      for line in lines:
        words = line.strip().split()
        for word in words:
          print(word,end=" ")
          time.sleep(0.1)








#conn.close()




#l = Library(0,"Langley")
# l.addbook()

# b1 = Book("difuihf",34270,"dbiewhf")
# b1.viewbooks()
#hw is to make a member class add orrowbook and return book methods in that class
#and keep trach of the number of books in library
#in book classevery book should have a property called availablity

class Member(Base):
    def __init__(self, name, age, department):
        super().__init__()
        self.name = name
        self.age = age
        self.department = department
        #self.borrowed_books = []

    def addmembertodb(self):
       self.cursor.execute("""CREATE TABLE IF NOT EXISTS Members(
        memberid INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        department TEXT
        
        
       )""")

       self.cursor.execute("""
       INSERT INTO Members (name,age,department)
       VALUES (?,?,?)

       """,(self.name,self.age,self.department))
       self.commit()
       print("Member added successfully")

    def viewbooks(self):
        self.cursor.execute("SELECT * FROM Members")
        data = self.cursor.fetchall()
        for i in data:
            print(i)

       
       

    def borrow_book(self, book):
        if book.ishere:
            self.borrowed_books.append(book)
            book.ishere = False
            print(f"{self.name} has borrowed '{book.title}'.")
            return True
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.ishere = True
            print(f"{self.name} has returned '{book.title}'.")
            return True
        else:
            print(f"{self.name} did not borrow '{book.title}'.")
            return False
        

        #use borrowed books table in boorrow book and rturn book methods

# Library.viewbooks()