import random
class Node(object):
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)
    def _insert(self,cur,key):
        if key < cur.data:
            if cur.left is None:
                cur.left = Node(key)
            else:
                self._insert(cur.left,key)
        else:
            if cur.right is None:
                cur.right = Node(key)
            else:
                self._insert(cur.right,key)
            
    def Min_Node(self):
        cur = self.root
        while(cur.left is not None):
            cur = cur.left
        return cur.data
    
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

tree = BST()
for i in range(0,10):
    r = random.randint(1,100)
    tree.insert(r)
tree.inorder()
print("\nNode with minimum value is ")
print(tree.Min_Node())
