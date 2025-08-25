class Complex:
    def __init__(self, real, imn):
        self.real=real
        self.imn=imn
        
    def display(self):
        print(self.real,"i +", self.imn, "j")
        
    def __add__(self,num2):#dunder function/operator overloading
        newreal=self.real+num2.real
        newimn=self.imn+num2.imn
        return Complex(newreal,newimn)
        
n1=Complex(4,5)
n1.display()

n2=Complex(7,2)
n2.display()

n3=n1+n2
n3.display()