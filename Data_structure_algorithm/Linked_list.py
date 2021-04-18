class Node:
    def __init__(self,data,next_node=None):
        self.data=data
        self.next_node=next_node

class Linked_list:
    def __init__(self):
        self.head=None

    #O(1)
    def insert_front(self,data):
        new_node=Node(data)
        
        if self.head==None:
            self.head=new_node
        else:
            new_node.next_node=self.head
            self.head=new_node

    #O(N)
    def insert_end(self,data):
        new_node=Node(data)
        current_node=self.head

        while current_node.next_node!=None:
            current_node=current_node.next_node
        current_node.next_node=new_node

    def delete(self,data):
        if self.head==None:
            return None

        current_node=self.head
        previous_node=None

        while current_node.data!=data:
            previous_node=current_node
            current_node=current_node.next_node

        if previous_node==None: #delete first data
            self.head=current_node.next_node
        else:
            previous_node.next_node=current_node.next_node
        
    def traverse(self):
        current_node=self.head
        
        print("Data:",end='')
        
        while current_node!=None:
            print(current_node.data,'',end='')
            current_node=current_node.next_node
            
