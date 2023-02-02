class calculation1:
    def sum(self,a,b):
        return a+b
class calculation2:
        def multiplication(self,a,b):
            return a*b
class derived(calculation1,calculation2):
         def div(self,a,b):
            return a/b

s=derived()
print(s.sum(10,2))
print(s.multiplication(30,20))
print(s.div(3,9))
print(issubclass(derived,calculation2))
print(issubclass(calculation1,calculation2))
print(isinstance(s,derived))