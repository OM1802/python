class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None
        self.count=0
        
    def is_empty(self):
        return self.count==0
        
    def enqueue(self,data):
        n=Node(data)
        if self.front is None:
            self.front=n
            self.rear=n
        else:
            self.rear.next=n
            self.rear=n
        self.count+=1
        
    def dequeue(self):
        if self.is_empty():
            print("QUEUE UNDERFLOW!!")
            return
        temp=self.front
        r=temp.item
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        self.count-=1
        print(f"REMOVED ELEMENT {r}", end="\n")
        
    def get_front(self):
        if self.count==0:
            print("EMPTY QUEUE!")
            return
        return self.front.item
        
    def get_rear(self):
        if self.count==0:
            print("EMPTY QUEUE!")
            return
        return self.rear.item
        
    def size(self):
        return self.count
        
    def display(self):
        if self.count==0:
            print("EMPTY QUEUE!")
            return
        print("FRONT-> ",end="")
        temp=self.front
        while temp is not None:
            print(temp.item,end="->" if temp.next else "")
            temp=temp.next
        print(" <-REAR")
        
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.size())
q.dequeue()
print(q.get_front())
print(q.get_rear())