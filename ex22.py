# student management system

class student:
    def __init__(self,usn,name,course):
        self.usn=usn
        self.name=name
        self.course=course

    def display(self):
        print(self.usn,self.name,self.course)

class studentmanager:
    def __init__(self):
        self.student=[]


    def add_student(self):
        usn=input("usn:")
        name=input("name:")
        course=input("course:")

        for students in self.student:
            if students.usn==usn:
                print("usn already exists")
                return

        self.student.append(
            student(usn,name,course)
        )
        print("student added")

    def view_students(self):
        if not self.student:
            print("no students found")
            return

        for student in self.student:
            student.display()

    def search_student(self):
        usn=input("search usn:")

        for student in self.student:
            if student.usn==usn:
                student.display()
                return

        print("student not found")

manager=studentmanager()

while True:
        print("\n---STUDENT MANAGEMENT---")
        print("1.AddStudent")
        print("2.ViewStudents") 
        print("3.SearchStudent") 
        print("4.Exit") 
        choice= input("Choice:") 
        if choice=="1": 
            manager.add_student() 
        elif choice=="2": 
            manager.view_students() 
        elif choice=="3": 
            manager.search_student() 
        elif choice=="4": 
            break 
        else: 
            print("InvalidChoice")