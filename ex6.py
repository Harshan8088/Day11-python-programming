# default constructor arguments

class course:
    def __init__(self,name="python"):
        self.name=name

    def display(self):
        print("course:",self.name)

c1=course()
c2=course("java")

c1.display()
c2.display()