# class with instance variable

class student:
    def set_details(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)

s1=student()
s1.set_details("ravi",21)
s1.display()