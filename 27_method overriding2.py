class bank: 
     def getroi(self):
         return 10
class SBI(bank):
       def getroi(self):
          return 7
class ICICI(bank):    
        def getroi(self):
             return 20

b1=bank()
b2=SBI()
b3=ICICI()
print("bank of interest : ",b1.getroi())
print("SBI of interest : ",b2.getroi())
print("ICICI of interest : ",b3.getroi())
