
print("interface having two abstrat method with one base class or sub class")
from abc import ABC,abstractmethod
class bank(ABC):
        @abstractmethod
        def balance_check(self):
            pass
        @abstractmethod
        def interest(self):
            pass
class SBI(bank):
        def balance_check(self):
            print("balance is 100 rupees")
        def interest(self):
            print("SBI bank interest is 5 rupees")
s=SBI()
s.balance_check() 
s.interest()       
        
