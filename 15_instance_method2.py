print("instance method using constructor")
class my_class1:
    def __init__(self,a,b):
         self.a=a
         self.b=b

    def instance_method(self):
           return f"this is a instance method and it can be access variable a={self.a} and b={self.b} with the help of self "

obj1=my_class1(2,4)          
print(obj1.instance_method())     