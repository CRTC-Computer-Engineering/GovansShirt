"""

This file contains all the calculations necessary
to provide totals and show processes along the way

"""
#Each list contains prices which start at Small and go to XLarge from left ot right
Small = True


Sweatshirt = [15,16,17,18]
Longsleeve = [12,13,14,15]
Shortsleeve = [10,11,12,14]
Clothing = ['Sweatshirt', 'Longsleeve', 'Shortsleeve']
#Red, Orange, Yellow, Green, Blue, Purple
Color = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
ColorPrice = [5,10,15,20,25,30]


def CalculatePrice():
    clothing = input("Cyka ")
    size = input("Blyat ")
    price = 0
    #Looking for Variables from GUI right here
    if clothing == Clothing[0]:
        if Small == True:
            price = price + Sweatshirt[0]
        elif Medium == True:
            price = price + Sweatshirt[1]
        elif Large == True:
            price = price + Sweatshirt[2]
        elif XLarge == True:
            price = price + Sweatshirt[3]
        else:
            print ("Errror")
    elif clothing == Clothing[1]:
        if Small == True:
            price = price + Longsleeve[0]
        elif Medium == True:
            price = price + Longsleeve[1]
        elif Large == True:
            price = price + Longsleeve[2]
        elif XLarge == True:
            price = price + Longsleeve[3]
        else:
            print ("Errror")
    elif clothing == Clothing[2]:
        if Small == True:
            price = price + Shortsleeve[0]
        elif Medium == True:
            price = price + Shortsleeve[1]
        elif Large == True:
            price = price + Shortsleeve[2]
        elif XLarge == True:
            price = price + Shortsleeve[3]
        else:
            print ("Errror")
    else:
        print ("Gay")
    if color == Color[0]:
        price = price +ColorPrice[0]
    elif color == Color[1]:
        price = price + ColorPrice[1]
    elif color == Color[2]:
        price = price + ColorPrice[2]
    elif color == Color[3]:
        price = price + ColorPrice[3]
    elif color == Color[4]:
        price = price + ColorPrice[4]
    elif color == Color[5]:
        price = price + ColorPrice[5]
    else:
        print ("Errror")

    print (price)
CalculatePrice()
