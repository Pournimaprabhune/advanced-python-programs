class my_class:
     def instance_method(self):
            return "this is  an instance"

obj=my_class()
print(obj.instance_method())
             
print("add other parameter with self")
class my_class1:

      def instance_method(self,a):
           return f"this is a instance method with a paratameter a={a}"

obj1=my_class1()          
print(obj1.instance_method(10))                
