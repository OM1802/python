class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left = left
        self.data = data
        self.right = right
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root is None:
            self.root = Node(None,data,None)
        else:
            self.rinsert(self.root,data)
            
    def rinsert(self,root,data):
        if data < root.data:
            if root.left is None:
                root.left = Node(None,data,None)
            else:
                self.rinsert(root.left,data)
        elif data > root.data:
            if root.right is None:
                root.right = Node(None,data,None)
            else:
                self.rinsert(root.right,data)
        else:
            pass
        
    def search(self,data):
        return self.rsearch(self.root,data)
        
    def rsearch(self,root,data):
        if root is None or root.data == data:
            return root
        if data > root.data:
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
    
    def minimum(self):
        return self._minimum(self.root)
        
    def _minimum(self,root):
        if root is None:
            return None
        while root.left:
            root=root.left
        return root
        
    def maximum(self):
        return self._maximum(self.root)
        
    def _maximum(self,root):
        if root is None:
            return None
        while root.right:
            root=root.right
        return root
            
    def delete(self,data):
        self.root=self.rdelete(self.root, data)
        
    def rdelete(self,root,data):
        if root is None:#UNDERFLOW CONDITION
            return root
        if data<root.data:
            root.left=self.rdelete(root.left,data)
        elif data>root.data:
            root.right=self.rdelete(root.right,data)
        else:#root==data
            #data has no child
            if root.right is None and root.left is None:
                return None
            #data has only 1 child    
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            #data had 2 child
            temp=self._minimum(root.right)#finding inorder successor
            root.data=temp.data#replacing the data with successor
            root.right=self.rdelete(root.right,temp.data)#deleting duplicate value of successor
            
        return root
        
    def size(self):
        return self.rsize(self.root)

    def rsize(self, root):
        if root is None:
            return 0
        return 1 + self.rsize(root.left) + self.rsize(root.right)
        
        
b = BST()

for x in [50, 30, 70, 20, 40, 60, 80]:
    b.insert(x)

print("Inorder   :", b.inorder())
print("Preorder  :", b.preorder())
print("Postorder :", b.postorder())

print("\nSearching 40:", "Found" if b.search(40) else "Not Found")
print("Searching 90:", "Found" if b.search(90) else "Not Found")

print("\nMinimum value in BST:", b.minimum().data)
print("Maximum value in BST:", b.maximum().data)

print("\nSize of BST:", b.size())

print("\nDeleting 70...")
b.delete(70)
print("Inorder after deletion:", b.inorder())

print("\nFinal Size:", b.size())
