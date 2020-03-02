class Stack:
    
    def __init__ (self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
        print("{} is pushed".format(item))
  
    def pop(self):
        popped=self.stack.pop()
        print("{} is popped".format(popped))
            
    def __call__ (self):
        print("Stack: {}".format(self.stack))
        
