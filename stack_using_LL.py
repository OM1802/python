class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class Stack:
    def __init__(self):
        self.top=None
        
    def is_empty(self):
        return self.top is None
        
    def push(self,data):
        n=Node(data)
        n.next=self.top
        self.top=n
        
    def pop(self):
        if self.is_empty():
            print("EMPTY STACK, OPERATION NOT POSSIBLE!!")
            return None
        else:
            self.top=self.top.next
            print("ELEMENT DELETED!!", end='\n')
            print()
        
    def peek(self):
        if self.is_empty():
            print("EMPTY STACK, OPERATION NOT POSSIBLE!!")
            return None
        else:
            print("THE TOP ELEMENT IS:",self.top.data, end='\n')
            print()
            
    def display(self):
        if self.is_empty():
            print("EMPTY STACK, OPERATION NOT POSSIBLE!!")
        else:
            temp=self.top
            print("ALL ELEMENTS IN STACK TOP TO BOTTOM:",end='\n')
            while temp is not None:
                print(temp.data, end='\n')
                temp=temp.next
                
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.peek()
s1.pop()
s1.peek()
s1.display()
        
        
