class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next
        
class Deque:
    def __init__(self,front=None, rear=None):
        self.front=None
        self.rear=None
        self.count=0
        
    def is_empty(self):
        return self.front is None
        
    def insert_front(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=self.rear=n
        else:
            n.next=self.front
            self.front.prev=n
            self.front=n
        self.count+=1
        
    def insert_rear(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=self.rear=n
        else:
            self.rear.next=n
            n.prev=self.rear
            self.rear=n
        self.count+=1
        
    def delete_front(self):
        if self.is_empty():
            print("EMPTY LIST!")
            return
        if self.front==self.rear:
            self.front=self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.count-=1
            
    def delete_rear(self):
        if self.is_empty():
            print("EMPTY LIST!")
            return
        if self.front==self.rear:
            self.front=self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.count-=1
        
    def get_front(self):
        if self.is_empty():
            print("EMPTY LIST!")
            return
        return self.front.data
        
    def get_rear(self):
        if self.is_empty():
            print("EMPTY LIST!")
            return
        return self.rear.data
        
    def size(self):
        return self.count
        
    def display(self):
        if self.is_empty():
            print("EMPTY LIST!")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
        

dq = Deque()
dq.insert_front(10)
dq.insert_front(20)
dq.insert_rear(30)
dq.display()          

dq.delete_front()
dq.display()          

dq.delete_rear()
dq.display()           

print("Front:", dq.get_front())  
print("Rear:", dq.get_rear())    
print("Size:", dq.size())        


            
