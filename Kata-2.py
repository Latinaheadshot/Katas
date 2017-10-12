# coding = utf-8
import math

def max(a,b):

    if a > b:
        mayor = a
    elif b > a:
        mayor = b
    elif int(a) == int (b):
        return (a)
    return mayor

max1 = max(5,5)
max2 = max(2,3)
max3 = max(int(max1),int(max2))

print (max3)