class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next
        
class DLL:
    def __init__(self):
        self.start=None
    
    def is_empty(self):
        return self.start is None
        
    def insert_first(self,data):
        n=Node(None,data,None)
        if self.is_empty():
            self.start=n
        else:
            self.start.prev=n
            n.next=self.start
            self.start=n
            
    def insert_last(self,data):
        n=Node(None,data,None)
        if self.start is None:
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            n.prev=temp
            
    def insert_at(self, data, target):
        temp = self.start
        while temp is not None:
            if temp.data == target:
                n = Node(temp, data, temp.next)
                if temp.next is not None:
                    temp.next.prev = n
                temp.next = n
                return
            temp = temp.next
        print("Target node not found!")
                    
    def search(self,data):
        while self.start is not None:
            temp=self.start
            while temp is not None:
                if temp.data==data:
                    print("ELEMENT AVAILABLE!")
                    return
                temp=temp.next
                
    def display(self):
        temp=self.start
        while temp is not None:
            print(temp.data, end="<->")
            temp=temp.next
        print("\n")
            
    def delete_first(self):
        if self.start is None:
            print("EMPTY LIST!!")
            return
        if self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next
            self.start.prev = None
                
    def delete_last(self):
        if self.start is None:
            print("EMPTY LIST!!")
            return
        if self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
            temp.prev=None
            
    def delete_node(self,data):
        if self.start is None:
            print("EMPTY LIST, NOTHING TO DELETE!!")
            return
        temp=self.start
        while temp is not None:
            if temp.data==data:
                break
            temp=temp.next
        if temp is None:
            print("ELEMENT NOT FOUND!!")
            return
            
        if temp.prev is None:#first node
            self.start=temp.next
            if temp.next is not None:
                temp.next.prev=None
        elif temp.next is None:#last node
            temp.prev.next=None
            temp.prev=None
        else:#middle node
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
            temp.next=None
            temp.prev=None
            

l=DLL()
l.insert_first(30)
l.insert_first(20)
l.insert_first(10)
l.insert_last(40)
l.insert_last(50)
l.insert_last(60)
l.display()
l.delete_first()
l.display()
l.delete_last()
l.display()
l.delete_node(30)
l.display()
l.insert_at(100,40)
l.display()
l.search(20)