class Stack(list):
    def is_empty(self):
        return len(self) == 0
        
    def push(self,data):
        self.append(data)
        
    def pop(self):
        if not self.is_empty():
            super().pop()
        else:
            raise IndexError("EMPTY STACK!!")
            
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("EMPTY STACK!!")
            
    def size(self):
        return len(self)
        
    def insert(self,index,data):
        raise AttributeError("No attribute 'insert' available in Stack")
        
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print(s1.peek())
s1.pop()
print(s1.peek())
print(s1.size())
            
    
