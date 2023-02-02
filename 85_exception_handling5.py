#python program to show how  touse assert keyword 
#defining a function
def sqaure_root(Number):
            assert(Number<0),"give a positive integer"
            return Number**(1/2)
#calling function and passing the values
print(sqaure_root(36))     
print(sqaure_root(-36))        