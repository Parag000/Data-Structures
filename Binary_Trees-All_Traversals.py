import random
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)    
    def _insert(self,cur,data):        
        if data < cur.data:
            if cur.left is None:
                cur.left = Node(data)
            else:
                self._insert(cur.left,data)
        else:
            if cur.right is None:
                cur.right = Node(data)
            else:
                self._insert(cur.right,data)
                
    def inorder(self):
        s = []
        cur = self.root
        while 1:
            if cur:
                s.append(cur)
                cur = cur.left
            elif s:
                cur = s.pop()
                print(cur.data,end = " ")
                cur = cur.right
            else:
                break
                
    def preorder(self):
        s = [] 
        s.append(self.root)
        while s:
            node = s.pop()
            print(node.data,end = " ")
            
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
                
    def postorder(self):
        s1 = []
        s2 = []
        s1.append(self.root)
        while s1:
            node = s1.pop()
            s2.append(node)

            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        while s2:
            node = s2.pop()
            print(node.data,end = " ")
            
    def lvlorder(self):
        q = []
        q.append(self.root)
        while q:
            print(q[0].data,end = " ")
            node = q.pop(0) 
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
b = BST()
for i in range(0,10):
    r = random.randint(1,50)
    b.insert(r)
print("INORDER TRAVERSAL")
b.inorder()
print("\nPREORDER TRAVERSAL")
b.preorder() 
print("\nPOSTORDER TRAVERSAL")
b.postorder()
print("\nLEVELORDER TRAVERSAL")
b.lvlorder()
