import ProjectSnippetVariables as psv
import HelperFunction as helper

def bookPortal():
    bookChoice = 0
    while(True):
        helper.cls()
        print(psv.bookPortalMessage)
        print("Enter choice")
        bookChoice = input(psv.booksSubMenu)

        #Check if the input is number is string or number befor type convrsion
        if(not bookChoice.isnumeric()):
            helper.cls()
            print(psv.bookSubMenuError,end="")
            continue

        #Convert The input into number
        bookChoice = int(bookChoice)

        #Add Book
        if(bookChoice == 1):
            helper.addBook()
            helper.cls()
            print("You Book is Added Successfully !!!!!")
            input("Press Any Key to Continue")

        #Update Book
        elif(bookChoice == 2): 
            helper.upadateBook()

        #Delete Book
        elif(bookChoice == 3): helper.deleteFromTable() # Delete 

        #View All Books
        elif(bookChoice == 4):
            helper.cls()
            helper.viewAllBooks()
           
        
        #Search Book
        elif(bookChoice == 5):
            helper.cls()
            helper.serachBook()
            input("Press Any Key to Continue")
            

        #Exit
        elif(bookChoice == 6):
            break

            
