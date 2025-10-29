"""
IMPORTED FILE SOURCE CODE:

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
                    

"""

from singly_ll import *
class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.item_count=0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if self.is_empty():
            print("EMPTY STACK!!")
            return
        else:
            self.mylist.delete_at_first()
            self.item_count-=1

    def peek(self):
        if self.is_empty():
            print("EMPTY STACK!!")
            return
        else:
            return self.mylist.start.data
        
    def size(self):
        return self.item_count
    

s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
s.pop()
print(s.peek())
print(s.size())

            
