class Node:
    def __init__(self,data,left_child=None,right_child=None):
        self.data=data
        self.left_child=left_child
        self.right_child=right_child

        
class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.insert_node(data,self.root)

    def insert_node(self,data,node):

        #left subtree

        if data<node.data:
            if node.left_child!=None:
                self.insert_node(data,node.left_child)
            else:
                node.left_child=Node(data)

        #right subtree
                
        else:
            if node.right_child!=None:
                self.insert_node(data,node.right_child)
            else:
                node.right_child=Node(data)

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

        return node
          
    def get_predecessor(self,node):
        if node.right_child!=None:
            return self.get_predecessor(node.right_child)
        return node

    def get_successor(self,node):
        if node.left_child!=None:
            return self.get_successor(node.left_child)
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
        
    def get_min(self):
        temp_node=self.root
        while temp_node.left_child!=None:
            temp_node=temp_node.left_child
        print("Minimum value:",temp_node.data)

    def get_max(self):
        temp_node=self.root
        while temp_node.right_child!=None:
            temp_node=temp_node.right_child
        print("Maximum value:",temp_node.data)

