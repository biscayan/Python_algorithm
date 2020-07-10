class Node:
    def __init__(self,name):
        self.name=name
        self.adjacencylist=[]
        self.visited=False
        self.predecessor=None

class BFS:
    def bfs(self,startnode):
        
        queue=[]
        queue.append(startnode)
        startnode.visited=True

        while queue: #while the queue is not empty
            actualnode=queue.pop(0) #FIFO structure
            print("{}".format(actualnode.name))

            for n in actualnode.adjacencylist: #neighbor check
                if n.visited==False:
                    queue.append(n)
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

    bfs=BFS()
    bfs.bfs(node1)

