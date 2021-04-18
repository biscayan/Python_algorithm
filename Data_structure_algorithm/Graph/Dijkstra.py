import sys
import heapq

class Node:
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.predecessor=None
        self.adjacencylist=[]
        self.mindistance=sys.maxsize

class Edge:
    def __init__(self,weight,startvertex,targetvertex):
        self.weight=weight
        self.startvertex=startvertex
        self.targetvertex=targetvertex

    def __cmp__(self,othervertex): #compare
        return self.cmp(self.mindistance,othervertex.mindistance)

    def __lt__(self,other): #less than
        selfpriority=self.mindistance
        otherpriority=other.mindistance
        return selfpriority < otherpriority

class Dijkstra:
    def calcshortestpath(self,vertexlist,startvertex):
        q=[]
        startvertex.mindistance=0
        heapq.heappush(q,startvertex)

        while q: #while q is not empty #len !=0 #>0
            actualvertex=heapq.heappop(q)

            for edge in actualvertex.adjacencylist:
                u=edge.startvertex
                v=edge.targetvertex

                newdistance=u.mindistance + edge.weight

                if newdistance<v.mindistance: #fine shorter path
                    v.mindistance=newdistance
                    v.predecessor=u
                    heapq.heappush(q,v)

    def getshortespath(self,targetvertex):
        print("Shortest path to vertex is {}".format(targetvertex.mindistance))

        node=targetvertex

        while node is not None:
            print("{}".format(node.name))
            node=node.predecessor

if __name__=='__main__':
    node1=Node("A")
    node2=Node("B")
    node3=Node("C")
    node4=Node("D")
    node5=Node("E")
    node6=Node("F")
    node7=Node("G")
    node8=Node("H")

    edge1=Edge(5,node1,node2)
    edge2=Edge(8,node1,node8)
    edge3=Edge(9,node1,node5)
    edge4=Edge(15,node2,node4)
    edge5=Edge(12,node2,node3)
    edge6=Edge(4,node2,node8)
    edge7=Edge(7,node8,node3)
    edge8=Edge(6,node8,node6)
    edge9=Edge(5,node5,node8)
    edge10=Edge(4,node5,node6)
    edge11=Edge(20,node5,node7)
    edge12=Edge(1,node6,node3)
    edge13=Edge(13,node6,node7)
    edge14=Edge(3,node3,node4)
    edge15=Edge(11,node3,node7)
    edge16=Edge(9,node4,node7)

    node1.adjacencylist.append(edge1)
    node1.adjacencylist.append(edge2)
    node1.adjacencylist.append(edge3)
    node2.adjacencylist.append(edge4)
    node2.adjacencylist.append(edge5)
    node2.adjacencylist.append(edge6)
    node8.adjacencylist.append(edge7)
    node8.adjacencylist.append(edge8)
    node5.adjacencylist.append(edge9)
    node5.adjacencylist.append(edge10)
    node5.adjacencylist.append(edge11)
    node6.adjacencylist.append(edge12)
    node6.adjacencylist.append(edge13)
    node3.adjacencylist.append(edge14)
    node3.adjacencylist.append(edge15)
    node4.adjacencylist.append(edge16)

    vertexlist=(node1,node2,node3,node4,node5,node6,node7,node8)

    dijkstra=Dijkstra()
    dijkstra.calcshortestpath(vertexlist,node1)
    dijkstra.getshortespath(node7)

    
