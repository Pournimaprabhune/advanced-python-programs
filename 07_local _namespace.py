def f():
     print('inititae f()')
     def g():
        print("initiate g()")
        print("end g()")
        return
     g()
     print("end f()")
     return
f()        