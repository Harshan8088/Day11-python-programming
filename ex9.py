# single inheritance

class person:
    def show_name(self):
        print("i am a person")

class student(person):
    def study(self):
        print("i am studying python")


s=student()
s.show_name()
s.study()