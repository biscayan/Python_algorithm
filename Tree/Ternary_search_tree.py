class Node:
    def __init__(self,character):
        self.character=character
        self.left_child=None
        self.right_child=None
        self.middle_child=None
        self.value=0

class TST:
    def __init__(self):
        self.root=None
    
    def put(self,key,value):
        self.root=self.put_item(self.root,key,value,0)
    
    def put_item(self,node,key,value,index):
        
        char=key[index]

        if node==None:
            node=Node(char) #create new node

        if char<node.character:
            node.left_child=self.put_item(node.left_child,key,value,index)
        elif char>node.character:
            node.right_child=self.put_item(node.right_child,key,value,index)
        elif index<len(key)-1:
            node.middle_child=self.put_item(node.middle_child,key,value,index+1)
        else:
            node.value=value
        
        return node

    def get(self,key):
        node=self.get_item(self.root,key,0)

        if node==None:
            return -1

        return node.value       

    def get_item(self,node,key,index):

        char=key[index]

        if node==None:
            return None

        if char<node.character:
            return self.get_item(node.left_child,key,index)
        elif char>node.character:
            return self.get_item(node.right_child,key,index)
        elif index<len(key)-1:
            return self.get_item(node.middle_child,key,index+1)
        else:
            return node
