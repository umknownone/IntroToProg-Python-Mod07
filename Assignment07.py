# ------------------------------------------------- #
# Title: Assignment07 - Python Error Handling and Pickling
# Description: Show how Python handles errors in code and
#               demonstrate how Pickling works in Python to
#               serialize/de-serialize a Python object structure
# ChangeLog: (Who, When, What)
# <Example Dev,01/01/2030,Created Script>
# DAlexandrov, 11.20.2019, Created Script
# ------------------------------------------------- #

import pickle

# -- Custom Exception -- #

class BinaryFileExtensionError(Exception): # custom exception if the file extension is not .dat
    def __str__(self):
        return "File Extension is invalid, expecting .dat"

class NonNumericInputError(Exception): # custom exception if the user inputs a non-numeric value
    def __str__(self):
        return "The user input was not numeric, please try again."

# -- Data -- #
lstData = []
dictRow = {}

# -- Presentation (I/O) -- #

def open_file(): # ask user for a file name
    file = input("What is the file name that you would like to open? *make sure it's a .dat file* ")
    return file

# -- Main Program -- #

while(True):
    print("Welcome to the Pickle Rick 3000: \n Here are your options: ")
    print("\t1: View My Data")
    print("\t2: Add Data")
    print("\t3: Pickle My Data")
    print("\t4: Unpickle My Data")
    print("\t5: Exit")
    strUserInput = input("What option do you want to choose? [1 - 5] ")

    if (strUserInput.strip() == "1"): # show current data in the list
        print("\nYour current data is: ")
        if not lstData:
            print("empty \n")
        else:
            for row in lstData:
                print(row)
            print("\n")
        continue

    elif (strUserInput.strip() == "2"): # let the user add an item to the list using a dictonary row
        strUserItem = input("What item would you like to add? ")
        strUserValue = input("What value would you like to assign to that item? ")
        print()
        dictRow = {"Item": strUserItem, "Value": strUserValue}
        lstData.append(dictRow)
        continue

    elif (strUserInput.strip() == "3"): # pickle the user data
        try:
            outputFile = open_file()
            if not outputFile.endswith(".dat"):
                raise BinaryFileExtensionError()
        except Exception as e:  # Custom Exception thrown
            print("An error has occurred...")
            print("The Custom Error info:")
            print(e)
            print("Please try again. \n")
            continue
        else:
            print("\nPickling your data...")
            objF = open(outputFile, "wb")
            pickle.dump(lstData, objF)
            objF.close()
            print("Your data has been pickled in the " + outputFile + " file. \n")
            continue

    elif (strUserInput.strip() == "4"): # unpicke the user data
        try:
            userFile = open_file()
            if not userFile.endswith(".dat"):
                raise BinaryFileExtensionError()
        except Exception as e:  # Custom Exception thrown
            print("An error has occurred...")
            print("The Custom Error info:")
            print(e)
            print("Please try again. \n")
            continue
        else:
            try:
                objF = open(userFile, "rb")
            except FileNotFoundError as e: # throw an exception when the file cannot be found
                print("An error has occurred...")
                print("The Built-in Python Error info:")
                print(e)
                print("Please try again. \n")
                continue
            else:
                output = pickle.load(objF)
                objF.close()
                lstData.append(output)
                print("\nYour un-pickled data is: ")
                print(output)
                print("\n")
                continue
    elif (strUserInput.strip() == "5"): # exit per user request
        exit()
    else:
        try:
            if not strUserInput.isnumeric():
                raise NonNumericInputError() # Throw custom non numeric input exception
        except NonNumericInputError as e:
            print("An error has occurred...")
            print("The Custom Error info:")
            print(e)
        finally:
            continue


