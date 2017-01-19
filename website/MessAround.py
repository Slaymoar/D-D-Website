
#Below the following code will:
#Prompt a user to enter names into a list
#When user types 'done' the program will alphabetize then display the list
#Program will then exit

##      NEW STEP
## Provide option to "save list" / "creat a new list"
## Once new list is created, provide a MENU to...
##    - View Lists
##    - Edit Lists
##    - Merge Lists

import os
os.system('clear')


    #TITLE HERE
print("")
print("")
print ("                Welcome to NAME LIST CREATOR!")
print ("")
print ("          To finish your list type 'done' at any time!")
print ("")

def mainMenu():
    print ("        Menu")
    print ("1. Create a list") #create new list
    print ("2. Load a previous list") #print old / created list from "saved"
    print ("3. Edit previous list")
    print ("4. Exit Program")



#Program Here
allNames = []
print ("Please enter the Names:")

#User input and 
def userInput():

    nameSTR = " "
    nameSTR = raw_input()
    
    nameSTR = nameSTR.strip()
    if not nameSTR or len(nameSTR) == 0:
        print("A name must have at least 1 character")
        userInput()

    # if nameSTR == " ":
    #     print ("A name must be at least 1 Letter, spaces will not be saved.")
    #     userInput()
    # if nameSTR == "":
    #     print ("A name must be at least 1 Letter, spaces will not be saved.")
    #     userInput()

    if nameSTR == "done":
        #capatalized names don't sort correctly
        sortedNames = sorted(allNames, key=lambda x: x.lower())

        print ("")
        print ("            Here's your list!")
        print ("")
        
        print (sortedNames)
        
        print ("")
        print ("    Thanks for using NAME LIST CREATOR!")
        print ("           Created by: Ian Berk")
        print("")
        print("")
        exit()

    else:
        allNames.append(nameSTR)
        userInput()

userInput()
