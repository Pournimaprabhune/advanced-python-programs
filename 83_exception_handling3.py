#python code to catch an exception and handle it using try and except code blocks
a=["python","Exceptions","try and except"]
try:
    #looping through the elements of the array a,choosing  a range that goes beyond the legth of arrray
    for i in  range(4):
               print("the index and elements from the array is:",i,a[i])
               #if an error occurs in the try block ,then except block will be excuted by the python interpreter
except:
      print(" index out of range")                  