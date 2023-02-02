class abc:
    def __init__(self):
        self.course="campus prepration"
        self.duration="2 month"
    def show(self):
      print("course",self.course)
      print("duration",self.duration)


outer=abc()
outer.show()
