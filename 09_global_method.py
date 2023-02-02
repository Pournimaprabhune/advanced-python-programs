print(type(globals()))
print(globals())
a=20
print(globals())
print(a)
print(globals()['a'])#value of a will be print
globals()['a']=100
print(globals())
print(a)