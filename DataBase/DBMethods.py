from DataBase.DBConnection import con,mydb
from DataBase import Queries as qu

def insertBook(bookTitle,book_author,book_publisher):
    con.execute(qu.ADD_BOOK_QUERY,(bookTitle,book_author,book_publisher))
    mydb.commit()

def getAllBooks():
    con.execute(qu.GET_ALL_BOOKS)
    return con.fetchall()

def serchBookInDB(bookName):
    con.execute(qu.SERCH_BOOK_BY_NAME +"'{}%'".format(bookName))
    return con.fetchall()

def isBookPresent(bookId):
    con.execute(qu.CHECH_BOOK_BY_BOOK_ID,(bookId,))
    return len(con.fetchall())

def updateBook(bookTitle, book_author, book_publisher,bookId):
    con.execute(qu.UPDATE_BOOK,(bookTitle, book_author, book_publisher,bookId))
    mydb.commit()

def deleteBook(bookId):
    con.execute(qu.DELTE_BOOK,(bookId,))
    mydb.commit()

