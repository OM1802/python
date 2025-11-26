class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left=left
        self.data=data
        self.right=right
        
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        if self.root is None:
            n=Node(None,data,None)
            self.root=n
        else:
            self.rinsert(self.root,data)
            
    def rinsert(self,root,data):
        if data<root.data:
            if root.left is None:
                root.left=Node(None,data,None)
            else:
                self.rinsert(root.left,data)
        elif data>root.data:
            if root.right is None:
                root.right=Node(None,data,None)
            else:
                self.rinsert(root.right,data)
        else:
            pass
        
    def search(self,data):
        return self.rsearch(self.root,data)
        
    def rsearch(self,root,data):
        if root is None or root.data==data:
            return root
        if data>root.data:
            return self.rsearch(root.right,data)
        else:
            return self.rsearch(root.left,data)
            
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
        
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.data)
            self.rinorder(root.right,result)
            
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
        
    def rpreorder(self,root,result):
        if root:
            result.append(root.data)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
            
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
        
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.data)
            


b = BST()

b.insert(50)
b.insert(30)
b.insert(70)
b.insert(20)
b.insert(40)
b.insert(60)
b.insert(80)

print(" Insertion Complete\n")

print("Inorder Traversal:  ", b.inorder())
print("Preorder Traversal: ", b.preorder())
print("Postorder Traversal:", b.postorder())

print("\n Traversals Complete\n")

key = 40
found = b.search(key)
if found:
    print(f"Search({key}): Found node with data =", found.data)
else:
    print(f"Search({key}): Not Found")

key = 100
found = b.search(key)
if found:
    print(f"Search({key}): Found node with data =", found.data)
else:
    print(f"Search({key}): Not Found")
 
        
        
