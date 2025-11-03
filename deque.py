class Deque:
    def __init__(self):
        self.mylist=[]
        self.count=0
        
    def is_empty(self):
        return len(self.mylist)==0
        
    def insert_front(self,data):
        self.mylist.insert(0,data)
        self.count+=1
        
    def insert_rear(self,data):
        self.mylist.append(data)
        self.count+=1
        
    def delete_front(self):
        if self.is_empty():
            print("NO ELEMENT TO DELETE!!")
            return
        self.mylist.pop(0)
        self.count-=1
        
    def delete_rear(self):
        if self.is_empty():
            print("NO ELEMENTS TO DELETE!!")
            return
        self.mylist.pop()
        self.count-=1
        
    def get_front(self):
        if self.is_empty():
            print("EMPTY LIST")
            return
        return self.mylist[0]
        
    def get_rear(self):
        if self.is_empty():
            print("EMPTY LIST")
            return
        return self.mylist[-1]
        
    def size(self):
        return self.count
        
q=Deque()
q.insert_front(10)
q.insert_rear(20)
q.insert_rear(30)
q.insert_rear(40)
q.insert_rear(50)
print("THE FRONT ELEMENT IS:",q.get_front())
print("THE REAR ELEMENT IS:",q.get_rear())
q.delete_front()
q.delete_rear()
print("THE FRONT ELEMENT IS:",q.get_front())
print("THE REAR ELEMENT IS:",q.get_rear())
print("THE SIZE OF DEQUE IS:",q.size())
