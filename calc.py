"""
This file contains all the calculations necessary
to provide totals and show processes along the way

"""
Color = 1
Size = 1
Type = 1

def CalculatePrice():
    price = TypePrice + ColorPrice + SizePrice
    print ("Type: " + type)
    print ("Color:" + color)
    print ("Size: " + size)
    print (str(TypePrice) + "+" + str(ColorPrice) "+" + str(SizePrice))
    print ("Cost: " + price)
