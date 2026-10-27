# upsate object data

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def increase(self,amount):
        self.salary +=amount


s1=employee("ravi",2000)
s1.increase(8000)

print("updated salary:",s1.salary)
