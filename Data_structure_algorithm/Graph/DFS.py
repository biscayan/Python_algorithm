class Node:
    def __init__(self,name):
        self.name=name
        self.adjacencylist=[]
        self.visited=False
        self.predecessor=None

#Recursive manner      
class DFS:
    def dfs(self,node):
        node.visited=True
        print("{}".format(node.name))

        for n in node.adjacencylist:
            if n.visited==False:
                self.dfs(n)
                
#It is also possible to implement with stack
class DFS:
    def dfs(self,startnode):
        
        stack=[]
        stack.append(startnode)
        startnode.visited=True

        while len(stack)!=0:#while the stack is not empty
            actualnode=stack.pop() #LIFO structure
            print("{}".format(actualnode.name))

            for n in actualnode.adjacencylist: #neighbor check
                if n.visited==False:
                    stack.append(n)
                    n.visited=True

                    
if __name__=='__main__':
    node1=Node("A")
    node2=Node("B")
    node3=Node("C")
    node4=Node("D")
    node5=Node("E")

    node1.adjacencylist.append(node2)
    node1.adjacencylist.append(node3)
    node2.adjacencylist.append(node4)
    node3.adjacencylist.append(node5)

    dfs=DFS()
    dfs.dfs(node1)
    
