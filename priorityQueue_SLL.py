class Node:
    def __init__(self,data=None,priority=None,next=None):
        self.data=data
        self.priority=priority
        self.next=next
        
class Pqueue:
    def __init__(self):
        self.start=None
        self.count=0
        
    def is_empty(self):
        return self.start is None
        
    def push(self,data,priority):
        n=Node(data,priority)
        if self.start is None or self.start.priority>priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next is not None and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.count+=1
        
    def pop(self):
        if self.is_empty():
            print("QUEUE UNDERFLOW CONDITION IDENTIFIED!!")
            return
        temp=self.start
        self.start=self.start.next
        print(f"POPED ELEMENT IS:({temp.data},{temp.priority})")
        self.count-=1
        return temp.data
        
    def size(self):
        return self.count
        
    def peek(self):
        if self.is_empty():
            print("QUEUE UNDERFLOW CONDITION IDENTIFIED!!")
            return None
        temp=self.start
        print(f"THE TOP PRIORITY ELEMENT IS: ({temp.data},{temp.priority})")
        return temp.data
    
    
pq=Pqueue()
pq.push("A", 3)
pq.push("B", 1)
pq.push("C", 2)

pq.peek()
pq.pop()
pq.peek()
print("Current Size:", pq.size())
