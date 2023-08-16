# Book Queries
ADD_BOOK_QUERY = '''
    INSERT INTO book(book_title, book_author, book_publisher)
    VALUES(%s,%s,%s)
                '''
GET_ALL_BOOKS = "SELECT * FROM book"
            
SERCH_BOOK_BY_NAME = " SELECT * FROM book WHERE book_title LIKE "

CHECH_BOOK_BY_BOOK_ID = " SELECT * FROM book WHERE bookId = %s"

UPDATE_BOOK = "UPDATE book SET book_title =%s, book_author =%s, book_publisher=%s  WHERE bookId=%s"

DELTE_BOOK = "DELETE FROM book WHERE bookId = %s"

