# employee salary 

class employee:
    def __init__(self,name,basic):
        self.name=name
        self.basic=basic

    def gross_salary(self):
        hra=self.basic*0.20
        da=self.basic*0.10
        return self.basic+hra+da

e = employee("kiran",25000)
print("gross salary:",e.gross_salary())