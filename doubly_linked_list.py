class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DLL:
    def __init__(self):
        self.start = None
        
    def is_empty(self):
        return self.start is None
        
    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n
        
    def insert_at_last(self, data):
        n = Node(None, data, None)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            n.prev = temp

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.data == data:
                print("ELEMENT FOUND")
                return
            temp = temp.next
        print("ELEMENT NOT FOUND")

    def insert_after(self,data,temp):
        temp=self.start
        while temp is not None:
            if temp.data==temp:
                n=Node(temp,data,temp.next)
                temp.next=n
                if temp.next is not None:
                    temp.next.prev=n
                    
    def display(self):
        temp=self.start
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.next
            
    def delete_first(self):
        while self.start is not None:
            temp=self.start
            if temp.next==None:
                self.start=None
            else:
                temp.next.prev=None
                self.start=temp.next
                
    def delete_last(self):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            temp.next.next.prev=None
            
    def delete_data(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None: