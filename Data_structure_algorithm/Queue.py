class Queue:
   
    def __init__ (self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)
        print("{} is enqueued".format(item))

    def dequeue(self):
        dequeued=self.queue.pop(0)
        print("{} is dequeued".format(dequeued))

    def __call__(self):
        print("Queue: {}".format(self.queue))
        

