print("\n python import statement \n")
import math
print(" the value of euler's number is",math.e)

print("\n importing and also renaming \n")
import math as mt
print(" the value of euler's number is",mt.e)


print("\n python from ... import statement \n")
from math import e
print(" the value of euler's number is",e)

print("\n python from... import statement both e and tau \n")
from math import e,tau
print(" the value of tau constant is\n",tau)
print(" the value of euler's number is\n",e)

print("import all names from import * statment")
from  math import *
print(" calculating square root",sqrt(25))
print(" calculating tangent of an angle:",tan(pi/6))

print("locating path of module")
import sys
print(sys.path)

print("the dir() built-in function")
print("list of function \n",dir(str),end=",")