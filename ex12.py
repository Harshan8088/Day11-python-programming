# multiple inheritance

class teacher:
    def teaching(self):
        print("teaching python")

class developer:
    def coding(self):
        print("developing applications")

class trainner(teacher, developer):
    pass

m1=trainner()
m1.teaching()
m1.coding()