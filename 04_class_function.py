class student:
      def __init__(self,name,id,age):
           self.name=name
           self.id=id
           self.age=age
      def display_details(self):
                 print("name :%s,id:%d,age:%d"%(self.name,self.id,self.age))

s=student("pournima",101,28)
print(s.__doc__)
print(s.__dict__)
print(s.__module__)
print(getattr(s,"name"))
print(getattr(s,"age"))
setattr(s,"age",29)
print(getattr(s,"age"))
print(hasattr(s,"id"))
delattr(s,"age")
print("age attribute will be deleted by delattr method/function ")

