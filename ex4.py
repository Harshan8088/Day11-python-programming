# constructor example

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name:",self.name)
        print("age:",self.age)

s1=student("priya",20)
s1.display()