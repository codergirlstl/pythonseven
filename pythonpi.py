import math

#Function that takes an input y and multiplies it by pi

#Ask the user for a number
y = float(input("Please give me a number: "))

#Define a function muptiply by pi
def resultpi(y):
    product = y * math.pi
    print(product)

resultpi(y)
