class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class SLL:
    def __init__(self,start=None):
        self.start=None
        
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
        
    def is_empty(self):
        return self.start is None
        
    def insert_at_end(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
            
    def search(self,data):
        temp=self.start
        while temp.next is not None:
            if temp.data==data:
                return temp
            temp=temp.next
        return None
        
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            
    def display(self):
        temp=self.start
        while temp is not None:
            print(temp.data, end=" ")
            temp=temp.next
        print(end="\n")
            
    def delete_at_first(self):
        if self.start is not None:
            self.start=self.start.next
            
    def delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is  None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            
    def delete_node(self,data):
        if self.start == None:
            pass
        elif self.start.next is None:
            if self.start.data==data:
                self.start=None
        else:
            temp=self.start
            if temp.data==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.data==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
                    
s=SLL()
s.insert_at_start(10)
s.insert_at_start(20)
s.insert_at_start(30)
s.display()
s.insert_at_end(40)
s.display()
n=s.search(10)
s.insert_after(n,50)
s.display()
s.delete_at_first()
s.display()
s.delete_at_last()
s.display()
s.delete_node(20)
s.display()