# multiple student objects

class student:
    def __init__(self,name,usn):
        self.name=name
        self.usn=usn

    def display(self):
        print(self.usn,"-",self.name)

students=[
    student("ravi","1sc001"),
    student("priya","1sc002"),
    student("kiran","1sc003")
]

for student in students:
    student.display()