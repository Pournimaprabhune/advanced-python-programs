from abc import ABC,abstractmethod
class polygon(ABC):
      @abstractmethod
      def sides(self):
            pass
class triangle(polygon):
       def sides(self):
            print("triangle has 3 sides")

class square(polygon):
       def sides(self):
            print("sqaure has 4 sides") 

class pentagon(polygon):
       def sides(self):
            print("pentagon has 5 sides")

class hexagon(polygon):
       def sides(self):
            print("hexagon has 6 sides")

t=triangle()
t.sides()
s=square()
s.sides()
p=pentagon()
p.sides()
h=hexagon()
h.sides()





