class XYZ():
    def website(self):
        print("javatpoint  is a website out of many avible on net")

    def topic(self):

          print("python is out of many topics about technology on javatpoint")
    
    def type(self):

         print("javatpoint is an developed website")

class PQR():

    def website(self):
        print("pinkvilla is a website out of many avible on net")

    def topic(self):

          print("celebrities is out of many topics about technology on javatpoint")
    
    def type(self):

         print("pinkvilla is an developed website")

def func(obj):
       obj.website()
       obj.topic()
       obj.type()

obj1=XYZ()
obj2=PQR()
func(obj1)
func(obj2)