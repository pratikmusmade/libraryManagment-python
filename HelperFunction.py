from DataBase import DBMethods as dbm
from prettytable import PrettyTable
import ProjectSnippetVariables as psv
import os


def cls():
    os.system('cls')

# Add Books


def addBook():
    cls()
    bookTitle = input("Enter Book Title \n")
    book_author = input("Enter Book Author \n")
    book_publisher = input("Enter Book Publisher \n")
    dbm.insertBook(bookTitle, book_author, book_publisher)

# View All Books
def viewAllBooks():
    printInTableFormat(dbm.getAllBooks())
    input("Press Any Key to Continue")


#Update Books
def upadateBook():
    print("See if the Book Exists !!")
    serachBook()
    bookId = input("Enter the Book to be updated")
    while(not bookId.isnumeric()):
        print("Please Enter integer value for book id")
        bookId = input("Enter the Book to be updated")
    bookId = int(bookId)

    if(not dbm.isBookPresent(bookId)): 
        print("The specified Book id does not exist")
        input("Press Enter Key to Go Back to the Menu")
        return
    

    bookTitle = input("Enter Book Title \n")
    book_author = input("Enter Book Author \n")
    book_publisher = input("Enter Book Publisher \n")
    dbm.updateBook(bookTitle, book_author, book_publisher,bookId)
    input("Book Updated Sccessfully \nPress Any Key to Continue")


#Search Book
def serachBook():
    bookName = input("Enter the name of the book")
    printInTableFormat(dbm.serchBookInDB(bookName))
    

#Print Book in tablar format

def printInTableFormat(bookList):
    tbl = PrettyTable(["bookId", "book_title", "book_author", "book_publisher"])
    print(bookList)
    #[(9, 'Data-Structures', 'newAuth', 'ATP'), (12, 'Demo1', 'authorDemo', 'pubDemo')]
    for bookId, book_title, book_author, book_publisher in bookList:
        tbl.add_row([bookId, book_title, book_author, book_publisher])
    print(psv.listOfBooks)
    print(tbl)

#Delete Book
def deleteFromTable():
    serachBook()
    bookId = input("Enter the Book to be deleted")

    while(not bookId.isnumeric()):
        print("Please Enter integer value for book id")
        bookId = input("Enter the Book to be updated")
    bookId = int(bookId)

    if(not dbm.isBookPresent(bookId)): 
        print("The specified Book id does not exist")
        input("Press Any Key to Go Back to the Menu")
        return
    
    dbm.deleteBook(bookId)