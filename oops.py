class Student:
    def __init__(self,fullname):#constructor
        self.name=fullname#Adding new student in database..
        
s1=Student("Max")
print(s1.name)