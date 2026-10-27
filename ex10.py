# parent and child constructor

class person:
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,usn):
        super().__init__(name)
        self.usn=usn

    def display(self):
        print(self.name,self.usn)

s=student("priya","1sc001")
s.display()
