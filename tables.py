"This file contains all the prices and calculations for the clothing"


Sweatshirt = [15,16,17,18]
Longsleeve = [12,13,14,15]
Shortsleeve = [10,11,12,14]
Clothing = ['Sweatshirt', 'Longsleeve', 'Shortsleeve']
#Red, Orange, Yellow, Green, Blue, Purple
Colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
ColorPrice = [5,10,15,20,25,30]
#One-Sided, Double-Sided
SidePrice = [2,4]
Sides = ['One-Sided' , 'Double-Sided']

#Small, Medium, Large, X-large
SizePrice = [15,15,15,17]
Sizes = ['Small', 'Medium', 'Large', 'X-Large']
def CalculatePrice(clothing, color, sides, size):
    clothing = Clothing[0]
    price = 0
    #Looking for Variables from GUI right here
    if clothing == Clothing[0]:
        if size == Sizes[0]:
            price = price + Sweatshirt[0]
        elif size == Sizes[1]:
            price = price + Sweatshirt[1]
        elif size == Sizes[2]:
            price = price + Sweatshirt[2]
        elif size == Sizes[3]:
            price = price + Sweatshirt[3]
        else:
            print ("Errror")
    elif clothing == Clothing[1]:
        if size == Sizes[0]:
            price = price + Longsleeve[0]
        elif size == Sizes[1]:
            price = price + Longsleeve[1]
        elif size == Sizes[2]:
            price = price + Longsleeve[2]
        elif size == Sizes[3]:
            price = price + Longsleeve[3]
        else:
            print ("Errror")
    elif clothing == Clothing[2]:
        if size == Shortsleeve[0]:
            price = price + Shortsleeve[0]
        elif size == Shortsleeve[1]:
            price = price + Shortsleeve[1]
        elif size == Shortsleeve[2]:
            price = price + Shortsleeve[2]
        elif size == Shortsleeve[3]:
            price = price + Shortsleeve[3]
        else:
            print("Errror")
    else:
        print (".")
    if color == Colors[0]:
        price = price + ColorPrice[0]
    elif color == Colors[1]:
        price = price + ColorPrice[1]
    elif color == Colors[2]:
        price = price + ColorPrice[2]
    elif color == Colors[3]:
        price = price + ColorPrice[3]
    elif color == Colors[4]:
        price = price + ColorPrice[4]
    elif color == Colors[5]:
        price = price + ColorPrice[5]
    else:
        print("Errror")

    if size == Sizes[0]:
        price = price + SizePrice[0]
    elif size == Sizes[1]:
        price = price + SizePrice[1]
    elif size == Sizes[2]:
        price = price + SizePrice[2]
    elif size == Sizes[3]:
        price = price + SizePrice[3]
    else:
        print("Error")


    if sides == Sides[0]:
        price = price + SidePrice[0]
    elif sides == Sides[1]:
        price = price + SidePrice[1]
    else:
        print("Error")


    print("Price: $" + str(price))

    return clothing
    return color
    return sides
    return size
