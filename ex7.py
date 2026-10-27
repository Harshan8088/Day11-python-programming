# instance and class variables

class student:
    college="search creators academy"

    def __init__(self,name):
        self.name=name

s1=student("rahul")
s2=student("priya")

print(s1.name,s1.college)
print(s2.name,s2.college)