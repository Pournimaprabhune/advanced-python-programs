tempretures=[10,-20,-289,100]
def abc(c):
       if c<-273.15:
          return "that tempreture doesn't make senesel"
       else:
         f=c*9/5+32
         return f

for t in tempretures:
                  print(abc(t))


