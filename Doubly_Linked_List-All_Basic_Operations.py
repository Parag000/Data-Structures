class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL(object):
    def __init__(self):
        self.head = None
    
    def infirst(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.prev = None
            new_node.next = None
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
    
    def inmid(self,prev_node,data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node
            
    def inlast(self,data):
        new_node = Node(data)
        temp = self.head
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        
    def dele(self,key):
        if self.head.data == key:
            self.head = self.head.next
            self.head.prev = None
        
        else:
            temp = self.head
            prev_node = temp
            while(temp.next):
                if temp.data == key:
                   prev_node.next = temp.next 
                   temp.next.prev = temp.prev 
                   break            
                prev_node = temp
                temp = temp.next
            if temp.next is None:
                self.delelast()
         
            
    def delelast(self):
        temp = self.head
        while(temp.next):
            prev_node = temp
            temp = temp.next
        prev_node.next = None
    
    
    def traverse(self,node):
        while(node is not None):
            print(node.data,end = " ")
            last = node
            node = node.next
        print()
        while(last is not None):
            print(last.data,end = " ")
            last = last.prev

l = DLL()
l.infirst(5)
l.infirst(4)  
l.infirst(3)  
l.infirst(2)
l.infirst(1) 
l.inmid(l.head.next,100) 
l.inlast(1000)
l.dele(100)
l.traverse(l.head) 
