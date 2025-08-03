#type - 1
number = 64
square = number**0.5
print("the square root of the given number is :",square)

#type - 2
number = 64
square = number**(1/2)
print("the square root of the given number is :",square)

#type - 3
import math
number = float(input("Enter a number for find the square root: "))
square = math.sqrt(number)
print(f"the square root of the given number is : %.3f" %square)

#type - 3
import cmath
number = int(input("Enter a number for find the square root: "))
square = cmath.sqrt(number)
print("the square root of the given number is : {0:.2}".format(square))