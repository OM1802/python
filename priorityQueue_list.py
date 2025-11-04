class Prqueue:
    def __init__(self):
        self.mylist=[]
        self.count=0
        
    def push(self,data,priority):
        index=0
        while index<len(self.mylist) and self.mylist[index][1]<=priority:
            index=index+1
        self.mylist.insert(index,(data,priority))
        self.count+=1
    
    def is_empty(self):
        return self.count==0
        
    def pop(self):
        if self.is_empty():
            print("QUEUE UNDERFLOW CONDITION IDENTIFIED!!")
            return
        self.mylist.pop(0)
        self.count-=1
        
    def peek(self):
        if self.is_empty():
            print("QUEUE UNDERFLOW CONDITION IDENTIFIED!!")
            return
        print(f"TOP PRIORITY ELEMENT IS: ({self.mylist[0][0],self.mylist[0][1]})")
        
    def size(self):
        return self.count
        
if __name__ == "__main__":
    pq = Prqueue()
    pq.push("A", 3)
    pq.push("B", 1)
    pq.push("C", 2)

    pq.peek()
    pq.pop()
    pq.peek()
    print("Current size:", pq.size())
    
        
