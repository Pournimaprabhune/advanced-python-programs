def scope_func():
    print("inside scope_func()")
    def scope_inner_func():
        var=20
        print("inside inner fuction ,value of var",var)
    scope_inner_func()
    #print("try printing var outer function",var)#var canout access outside function becoz its scope is limited to scope_ineer_func() and var=20 is loacal
scope_func()