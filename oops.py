class Student:
    def __init__(self,name,marks):#constructor
        self.name=name
        self.marks=marks
    
    @staticmethod #decorator
    def hello():
        print("HELLO!! ")
        
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(sum/3)
        

s1=Student("BEN", [85,25,46])
s1.hello()
s1.get_avg()