# Persoanl data existance in database
Q = int(input("Enter quantity of people: "))
Dict = {}
for i in range(1, Q+1):
    FName = input("Enter name: ")
    CN = input("Enter card number: ")
    Password = input("Enter password: ")
    Dict[i+1] = {"FName":FName, "CN":CN, "Password":Password}
# Language selection
# A tuple for language and unpacking process
Language = ("Persian", "English")
("1", "2") == Language
# Display of language on screen for user
print ("1: ", Language[0])
print ("2: ", Language[1])
L = input("Please choose your language: ")
if L == "1":
    print ("Language: ", Language[0])
elif L == "2":
    print ("Language: ", Language[1])
print()
# Start ATM operation
i = int(input("Enter resident number: "))
counter = 1
while counter <= 2:
    #Calling from database was required in this section
    Password = input ("Enter your password: ")
    if Password in Dict[i+1]["Password"]:
        print()
        # A tuple for operation items and unpacking process
        Operation_Items = ("Transfer Operation", "Change Password", "Bill Operation")
        ("1", "2", "3") == Operation_Items
        # Display of ATM operations on screen for user
        print ("1: ", Operation_Items[0])
        print ("2: ", Operation_Items[1])
        print ("3: ", Operation_Items[2])
        Operation = input("Operation Selection: ")
        print()
        if Operation == "1":
            # A tuple for prices and unpacking process
            Prices = ("200000 Rials", "800000 Rials", "1000000 Rials", "Other Price")
            # Display of prices on screen for user
            ("1", "2", "3", "4") == Prices
            print ("1: ", Prices[0])
            print ("2: ", Prices[1])
            print ("3: ", Prices[2])
            print ("4: ", "Other Price")
            print()
            # Selection of prices or enter user's considered proces
            x = input("Please select your price: ")
            if x == "1":
                CN = input("Enter destination card number: ") # CN = Card Number
                print ("Destination card number is: ", CN)
            elif x == "2":
                CN = input("Enter destination card number: ") # CN = Card Number
                print ("Destination card number is: ", CN)
            elif x == "3":
                CN = input("Enter destination card number: ") # CN = Card Number
                print ("Destination card number is: ", CN)
            elif x == "4":
                print (input("Enter your price: "))
                CN = input("Enter destination card number: ") # CN = Card Number
                print ("Destination card number is: ", CN)
            print()
            Answer = ("Yes", "No")
            ("1", "2") == Answer
            print("1: ", Answer[0])
            print("2: ", Answer[1])
            y = input("Do you certain about destination card number? ")
            if y == "1":
                print("Operation was done successfully")
                break
            elif y == "2":
                print("Please enter right destination card number and do again")
        elif Operation == "2":
            # Selection of second operation about change password of card number
            input("Enter your current password: ")
            input("Enter new password: ")
            input("Enter again new password: ")
            print("Your password was changed successfully")
            break
        elif Operation == "3":
            input("Enter destination bank name: ")
            break
    else:
        if counter == 1:
            print()
            print("Please insert the correct password and try again !")
            counter += 1
        elif counter == 2:
            print()
            print("Authorized counter of password was finished !")
            counter += 1
