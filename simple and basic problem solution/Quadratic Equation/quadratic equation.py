import cmath
a = int(input("Enter number of a : "))
while a==0:
    print("value of a can't 0")
    a = int(input("Enter another number of a :"))
else:
    b = int(input("Enter number of b : "))
    c = int(input("Enter number of c : "))
d = (b**2) - 4*a*c
root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)
print("The roots are {0:.2} and {1:.2}".format(root1,root2))