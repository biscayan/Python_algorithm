class Node:
    def __init__(self,data,left_child=None,right_child=None):
        self.data=data
        self.left_child=left_child
        self.right_child=right_child
        self.height=0

class AVL:
    def __init__(self):
        self.root=None

    def calc_height(self,node):
        if node==None:
            return -1

        return node.height

    def balance_factor(self,node):
        if node==None:
            return 0

        return self.calc_height(node.left_child)-self.calc_height(node.right_child)

    def insert(self,data):
        self.root=self.insert_node(data,self.root)

    def insert_node(self,data,node):

        if node==None:
            return Node(data)

        # left subtree
        
        if data<node.data:
            node.left_child=self.insert_node(data,node.left_child)

        # right subtree

        else:
            node.right_child=self.insert_node(data,node.right_child)
            
        node.height=max(self.calc_height(node.left_child),
                        self.calc_height(node.right_child))+1
        
        return self.settle_unbalance(data,node)

    def delete(self,data):
        if self.root!=None:
            self.root=self.delete_node(data,self.root)
            
    def delete_node(self,data,node):
        if node==None:
            return node
        
        if data<node.data:
            node.left_child=self.delete_node(data,node.left_child)

        elif data>node.data:
            node.right_child=self.delete_node(data,node.right_child)

        else:
            # Case1.The node is a leaf node
            if node.left_child==None and node.right_child==None:
                print("Delete the node which is a leaf node")
                del node
                return None

            # Case2. The node has a single child
            # Case2-1. The node has a single left child
            elif node.right_child==None:
                print("Delete the node which has a single left child")
                temp_node=node.left_child
                del node
                return temp_node

            # Case2-2. The node has a single right child
            elif node.left_child==None:
                print("Delete the node which has a single right child")
                temp_node=node.right_child
                del node
                return temp_node

            # Case3. The node has two children
            else:
                print("Delete the node which has two children")
                temp_node=self.get_predecessor(node.left_child)
                node.data=temp_node.data
                node.left_child=self.delete_node(temp_node.data,node.left_child)
                return node

        if node==None:
            return node

        node.height=max(self.calc_height(node.left_child),
                        self.calc_height(node.right_child))+1

        balance=self.balance_factor(node)

        # Case1. left left situation

        if balance>1 and self.balance_factor(node.left_child)>=0:
            self.right_rotation(node)

        # Case2. right right situation

        if balance<-1 and self.balance_factor(node.right_child)<=0:
            self.left_rotation(node)

        # Case3. left right situation

        if balance>1 and self.balance_factor(node.left_child)<0:
            node.left_child=self.left_rotation(node.left_child)
            self.right_rotation(node)
            
        # Case4. right left situation

        if balance<-1 and self.balance_factor(node.right_child)>0:
            node.right_child=self.right_rotation(node.right_child)
            self.left_rotation(node)

        return node
          
    def get_predecessor(self,node):
        if node.right_child!=None:
            return self.get_predecessor(node.right_child)
        return node

    def get_successor(self,node):
        if node.left_child!=None:
            return self.get_successor(node.left_child)
        return node

    def right_rotation(self,node):
        
        # right rotation for solving left heavy situation
        
        print("Rotating to the right")

        temp_left_child=node.left_child
        moved_node=temp_left_child.right_child
        temp_left_child.right_child=node
        node.left_child=moved_node

        node.height=max(self.calc_height(node.left_child),
                        self.calc_height(node.right_child))+1

        temp_left_child.height=max(self.calc_height(temp_left_child.left_child),
                                   self.calc_height(temp_left_child.right_child))+1

        return temp_left_child
    
    def left_rotation(self,node):
        
        # left rotation for solving right heavy situation
        
        print("Rotating to the left")

        temp_right_child=node.right_child
        moved_node=temp_right_child.left_child
        temp_right_child.left_child=node
        node.right_child=moved_node

        node.height=max(self.calc_height(node.left_child),
                        self.calc_height(node.right_child))+1

        temp_right_child.height=max(self.calc_height(temp_right_child.left_child),
                                    self.calc_height(temp_right_child.right_child))+1

        return temp_right_child
    
    def settle_unbalance(self,data,node):

        balance=self.balance_factor(node)

        # Case1. left left situation

        if balance>1 and data<node.left_child.data:
            print("left left heavy tree")
            return self.right_rotation(node)
            
        # Case2. right right situation

        if balance<-1 and data>node.right_child.data:
            print("right right heavy tree")
            return self.left_rotation(node)

        # Case3. left right situation

        if balance>1 and data>node.left_child.data:
            print("left right heavy tree")
            node.left_child=self.left_rotation(node.left_child)
            return self.right_rotation(node)

        # Case4. right left situation

        if balance<-1 and data<node.right_child.data:
            print("right left heavy tree")
            node.right_child=self.right_rotation(node.right_child)
            return self.left_rotation(node)

        return node

    def inorder_traversal(self):
        print("Inorder traversal: ",end='')
        
        def inorder_traversal(root):
            if root!=None:
                if root.left_child!=None:
                    inorder_traversal(root.left_child)

                print(root.data,end=' ')
                    
                if root.right_child!=None:
                    inorder_traversal(root.right_child)
                    
        inorder_traversal(self.root)
        print()
        
    def preorder_traversal(self):
        print("Preorder traversal: ",end='')
        
        def preorder_traversal(root):
            print(root.data,end=' ')
            
            if root!=None:
                if root.left_child!=None:
                    preorder_traversal(root.left_child)
                    
                if root.right_child!=None:
                    preorder_traversal(root.right_child)
                    
        preorder_traversal(self.root)
        print()
        
    def postorder_traversal(self):
        print("Postorder traversal: ",end='')
        
        def postorder_traversal(root):
            if root!=None:
                if root.left_child!=None:
                    postorder_traversal(root.left_child)
                    
                if root.right_child!=None:
                    postorder_traversal(root.right_child)

            print(root.data,end=' ')
                    
        postorder_traversal(self.root)
        print()

