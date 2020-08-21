class Node(object):
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

class BST(object):
    def __init__(self):
        self.root = None
    
    def LCA(self,n1,n2):
        cur = self.root
        while cur:
            if n1 < cur.data and n2 < cur.data:
                cur = cur.left
            elif n1 > cur.data and n2 > cur.data:
                cur = cur.right
            else:
                break
        return cur.data
        
tree = BST()
tree.root = Node(20) 
tree.root.left = Node(8) 
tree.root.right = Node(22) 
tree.root.left.left = Node(4) 
tree.root.left.right = Node(12) 
tree.root.left.right.left = Node(10) 
tree.root.left.right.right = Node(14) 
print("\nLowest Common Ancestor ")
print(tree.LCA(10,14))    
