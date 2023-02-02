class employee:
    _count=0
    def __init__(self):
        employee._count=employee._count+1
    def display(self):
        print("the number of employee count : ",employee._count)

emp=employee()
emp1=employee()
try:
    print(emp._count)
finally:
       emp.display()    