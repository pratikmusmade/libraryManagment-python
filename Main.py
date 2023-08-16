import ProjectSnippetVariables as psv
import HelperFunction as helper
import BookPortal as bp
print("This is a python project")
mainMenuChoice = 0
# print(mainMenuChoice)
while(True):
    helper.cls()
    print(psv.intoMessage,end="")
    print(psv.mainMenu)
    mainMenuChoice = input(psv.menuMessage)

    if(not mainMenuChoice.isnumeric()):
        print(psv.choiceErrorMessage,end="")
        input("Press Enter key to Continue")
        continue

    mainMenuChoice = int(mainMenuChoice)
    if(mainMenuChoice == 1): bp.bookPortal()
    elif(mainMenuChoice == 2) : pass
    elif(mainMenuChoice == 3):break


