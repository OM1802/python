class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class CLL:
    def __init__(self):
        self.last=None
        
    def is_empty(self):
        return self.last is None
        
    def insert_first(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    
    def insert_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
            
    def insert_after(self,data,temp):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
                
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while True:
            if temp.data==data:
                return temp
            temp=temp.next
            if temp==self.last.next:
                break
        return None
        
    def display(self):
        if self.is_empty():
            print("EMPTY LIST!")
            return
        
        temp=self.last.next
        while True:
            print(temp.data, end=" ->")
            temp=temp.next
            if temp==self.last.next:
                print("BACK TO FIRST NODE")
                break
    
    def delete_first(self):
        if self.is_empty():
            return
        if self.last.next==self.last:
            self.last=None
        else:
            self.last.next=self.last.next.next
            
    def delete_last(self):
        if self.is_empty():
            return
        if self.last==self.last.next:
            self.last=None
        else:
            temp=self.last.next
            while temp.next!=self.last:
                temp=temp.next
            temp.next=self.last.next
            self.last=temp
    
    def delete_node(self,data):
        if self.is_empty():
            return
        if self.last==self.last.next:
            if self.last.data==data:
                self.last=None
                print("NODE DELETED!")
                return
        temp=self.last.next
        while temp.next != self.last:
            if temp.next.data==data:
                temp.next=temp.next.next
                print("NODE DELETED!")
                return
            temp=temp.next
            
        if self.last.data==data:
            temp.next=self.last.next
            self.last=temp
            print("NODE DELETED!!")
            
c=CLL()
c.insert_first(10)
c.insert_last(20)
c.insert_last(30)
c.insert_last(40)
c.insert_last(50)
c.display()
c.insert_after(35,c.search(30))
c.display()
c.delete_first()
c.display()
c.delete_last()
c.display()
c.delete_node(35)
c.display()
