class Accounts:
    def __init__(self,bal,ac_no):
        self.bal=bal
        self.ac_no=ac_no
        
    def debit(self):
        d=int(input("ENTER THE AMOUNT TO DEBIT: "))
        if d>self.bal:
            print("INSUFFICIENT AMOUNT!")
        else:
            self.bal=self.bal-d
            print("TRANSACTION COMPLETE RS ",d,"WAS DEBITED FROM YOUR ACCOUNT")
            
    def credit(self):
        c=int(input("ENTER THE AMOUNT TO CREDIT: "))
        self.bal=self.bal+c
        print("RS ",c,"IS CREDITED INTO YOUR ACCOUNT. ")
        
    def print_bal(self):
        ac=int(input("ENTER YOUR ACCOUNT NUMBER: "))
        if ac==self.ac_no:
            print(self.bal)
        else:
            print("WRONG ACCOUNT NUMBER")
            
a1=Accounts(50000, 2580)
a1.debit()
a1.credit()
a1.print_bal()
        
        