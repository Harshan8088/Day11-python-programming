# multilevel inheritance

class person:
    def identity(self):
        print("person")

class employee(person):
    def work(self):
        print("employee")

class manager(employee):
    def manage(self):
        print("manager")


m=manager()
m.identity()
m.work()
m.manage()