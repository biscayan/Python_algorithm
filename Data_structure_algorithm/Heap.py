class Heap:
    
    capacity=10

    #create an empty array
    def __init__(self):
        self.heap=[0]*self.capacity
        self.heap_size=0

    def insert(self,item):
        if self.heap_size==self.capacity:
            print("Heap is full")
            return None
        
        self.heap[self.heap_size]=item
        self.heap_size+=1
        self.fix_up(self.heap_size-1)

    #O(logN)
    def fix_up(self,index):
        
        parent_index=int((index-1)/2)
        
        if index>0 and self.heap[index]>self.heap[parent_index]:
            self.swap(index,parent_index)
            self.fix_up(parent_index)

    def swap(self,index1,index2):
        self.heap[index1],self.heap[index2]=self.heap[index2],self.heap[index1]

    #O(logN)
    def poll(self):

        max_value=self.heap[0]

        #swap root and final element
        self.swap(0,self.heap_size-1)
        self.heap_size-=1

        self.fix_down(0)
        
        return max_value

    def fix_down(self,index):

        left_index=2*index+1
        right_index=2*index+2

        largest_index=index

        if left_index<self.heap_size and self.heap[left_index]>self.heap[index]:
            largest_index=left_index

        if right_index<self.heap_size and self.heap[right_index]>self.heap[index]:
            largest_index=right_index

        if index != largest_index:
            self.swap(index,largest_index)
            self.fix_down(largest_index)

    #O(NlonN)
    def heap_sort(self):

        for i in range(0,self.heap_size):
            max_value=self.poll()
            print(max_value)
