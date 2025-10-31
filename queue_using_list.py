class Queue:
    def __init__(self):
        self.mylist=[]
        self.front=None
        self.rear=None
        
    def is_empty(self):
        return len(self.mylist) == 0
        
    def enqueue(self,data):
        self.mylist.append(data)
        print("ENQUEUE OPERATION PERFORMED SUCCESSFULLY", end='\n')
        self.rear=data
        if self.front is None:
            self.front=data
            
            
    def dequeue(self):
        if self.is_empty():
            print("QUEUE UNDERFLOW. DEQUEUE NOT POSSIBLE!!")
            return
        self.mylist.pop(0)#from collections import dequeue self.mylist.popleft() //for O(1)
        print("DEQUEUE OPERATION PERFORMED SUCCESSFULLY", end='\n')
        if len(self.mylist)==0:
            self.front=self.rear=None
        elif len(self.mylist)==1:
            self.front=self.rear=self.mylist[0]
        else:
            self.front=self.mylist[0]
            self.rear=self.mylist[-1]
            
    def get_front(self):
        if self.is_empty():
            print("EMPTY QUEUE!")
            return
        return self.front
        
    def get_rear(self):
        if self.is_empty():
            print("EMPTY QUEUE!")
            return
        return self.rear
        
    def size(self):
        return len(self.mylist)
        
    def display(self):
        if self.is_empty():
            print("EMPTY QUEUE.")
            return
        print(list(self.mylist))
        

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("THE FRONT IS:",q.get_front(), end='\n')
print("THE REAR IS:",q.get_rear(), end='\n')
q.dequeue()
print("THE FRONT IS:",q.get_front(), end='\n')
print("THE REAR IS:",q.get_rear(), end='\n')
print("SIZE OF THE QUEUE IS:",q.size(),end='\n')

        
    
            
        
        
