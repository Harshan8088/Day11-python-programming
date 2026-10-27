# student result calculator

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def result(self):
        total=sum(self.marks)
        percentage=total/len(self.marks)

        print("student:",self.name)
        print("toatl:",total)
        print("percentage:",percentage)

        if all(m>=35 for m in self.marks):
            print("pass")
        else:
            print("fail")


s=student("rahul",[90,35,78,94,83])
s.result()