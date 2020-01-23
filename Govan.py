"""
Made By Aidan Boucher
"""
import Tables

def blankline(lines):
    for i in range(lines):
        print (""" """)

def separation():
    print("==================================================")



print ("Welcome to the shirt price generator!")
blankline(1)

separation()
#print("How many items are you ordering today?")
#orders = int(input("Please type the number of the choice: "))
separation()

blankline(2)
def Questions():

    separation()
    print("What type of clothing would you like to design? ")
    print("1. Sweatshirt")
    print("2. Longsleeve Shirt")
    print("3. Shortsleeve Shirt")
    separation()


    while True:
        try:
            typechoice = int(input("Please type the number of the choice: "))
            if typechoice == 1:
                clothing = Tables.Clothing[0]
                print("You selected Sweatshirt!")
                break
            elif typechoice == 2:
                clothing = Tables.Clothing[1]
                print("You selected Longsleeve Shirt!")
                break
            elif typechoice == 3:
                clothing = Tables.Clothing[2]
                print("You selected Shortsleeve Shirt!")
                break
            else:
                print("That is not a valid response.")
                continue
        except ValueError:
            print("That is not a valid response. Try using NUMBERS!")
            continue


    blankline(2)
    separation()
    print("What color would you like your " + clothing + " to be?")
    print("1. Red")
    print("2. Orange")
    print("3. Yellow")
    print("4. Green")
    print("5. Blue")
    print("6. Purple")
    separation()

    while True:
        try:
            colorchoice = int(input("Please type the number of the choice: "))
            if colorchoice == 1:
                color = Tables.Colors[0]
                print("You selected Red!")
                break
            elif colorchoice == 2:
                color = Tables.Colors[1]
                print("You selected Orange!")
                break
            elif colorchoice == 3:
                color = Tables.Colors[2]
                print("You selected Yellow!")
                break
            elif colorchoice == 4:
                color = Tables.Colors[3]
                print("You selected Green!")
                break
            elif colorchoice == 5:
                color = Tables.Colors[4]
                print("You selected Blue!")
                break
            elif colorchoice == 6:
                color = Tables.Colors[5]
                print("You selected Purple!")
                break
        except ValueError:
            print("That is not a vaid response. Try using NUMBERS!")
            continue

    blankline(2)
    separation()
    print("Would you like to print 1 or 2 sides on your " + color + " " + clothing + " to be?")
    print("1. One-Sided")
    print("2. Double-Sided")
    separation()

    while True:
        try:
            sidechoice = int(input("Please type the number of the choice: "))
            if sidechoice == 1:
                sides = Tables.Sides[0]
                print("You selected One-Sided")
                break
            elif sidechoice == 2:
                sides = Tables.Sides[1]
                print("You selected Double-Sided")
                break
            else:
                print("That is not a valid response. Try using NUMBERS!")
        except ValueError:
            print("That is not a valid response. Try using NUMBERS!")
            continue
    blankline(2)
    separation()
    print("What size would you like your " + sides + " " + color + " " + clothing + " to be?")
    print("1. Small")
    print("2. Medium")
    print("3. Large")
    print("4. X-Large")
    separation()

    while True:
        try:
            sizechoice = int(input("Please type the number of the choice: "))
            if sizechoice == 1:
                size = Tables.Sizes[0]
                print("You selected Small!")
                break
            elif sizechoice == 2:
                size = Tables.Sizes[1]
                print("You selected Medium")
                break
            elif sizechoice == 3:
                size = Tables.Sizes[2]
                print("You selected Large")
                break
            elif sizechoice == 4:
                size = Tables.Sizes[3]
                print("You selected X-Large")
                break
        except ValueError:
            print("That is not a valid response. Try using NUMBERS!")
            continue

    blankline(2)

    print("You are ordering a " + sides + ", " + size + ", " + color + " " + clothing + "!")


    Tables.CalculatePrice(clothing, color, sides, size)


#for i in range(orders):

    #Questions()
Questions()
