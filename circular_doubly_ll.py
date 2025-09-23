class Node:
    def __init__(self,prev=None, data=None, next=None):
        self.prev=prev
        self.data=data
        self.next=next
        
class CDLL:
    def __init__(self):
        self.start=None
        
    def is_empty(self):
        return self.start is None
        
    def insert_first(self,data):
        n=Node(None,data,None)
        if self.is_empty():
            n.prev=n
            n.next=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
        
    def insert_last(self,data):
        n=Node(None,data,None)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
            
    def search(self, data):
        if self.is_empty():
            print("EMPTY LIST!!")
            return
        else:
            temp=self.start
            while True:
                if temp.data==data:
                    return temp
                temp=temp.next
                if temp==self.start:
                    break
            print("DATA NOT FOUND!!")
            return
        
    def insert_after(self,data,temp):
        if temp is not None:
            n=Node(None,data,None)
            n.prev=temp
            n.next=temp.next
            temp.next=n
            temp.next.prev=n
                
    def display(self):
        if self.is_empty():
            print("EMPTY LIST!!")
            return
        temp=self.start
        while True:
            print(temp.data, end="<=>")
            temp=temp.next
            if temp is self.start:
                break
            
    def delete_first(self):
        if self.is_empty():
            print("EMPTY LIST!!")
            return
        if self.start.next == self.start:
            self.start=None
        else:
            self.start.prev.next=self.start.next
            self.start.next.prev=self.start.prev
            self.start=self.start.next
            
    def delete_last(self):
        if self.is_empty():
            print("EMPTY LIST!!")
            return
        if self.start.next==self.start:
            self.start=None
        else:
            self.start.prev.prev.next=self.start
            self.start.prev=self.start.prev.prev
            
    def delete_node(self, data):
        if self.is_empty():
            print("EMPTY LIST!!")
            return

        if self.start.next == self.start:
            if self.start.data == data:
                self.start = None
                return
            else:
                print("ELEMENT NOT FOUND!!")
                return

        temp = self.start
        while True:
            if temp.data == data:
                if temp == self.start:
                    self.start = self.start.next
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return
            temp = temp.next
            if temp == self.start: 
                break

        print("ELEMENT NOT FOUND!!")
    
    
l=CDLL()
l.insert_first(10)
l.insert_last(20)
l.insert_last(30)
l.insert_after(25,l.search(20))
#l.delete_first()
l.delete_node(20)
l.display()
        
