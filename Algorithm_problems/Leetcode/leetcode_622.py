class MyCircularQueue:

    def __init__(self, k: int):
        self.cir_queue = [None] * k
        self.max_len = k
        self.f_pointer = 0
        self.r_pointer = 0

    def enQueue(self, value: int) -> bool:
        if self.cir_queue[self.r_pointer] == None:
            self.cir_queue[self.r_pointer] = value
            self.r_pointer = (self.r_pointer+1) % self.max_len
            return True
        else:
            return False
            
    def deQueue(self) -> bool:
        if self.cir_queue[self.f_pointer] == None:
            return False
        else:
            self.cir_queue[self.f_pointer] = None
            self.f_pointer = (self.f_pointer+1) % self.max_len
            return True

    def Front(self) -> int:
        if self.isEmpty() == True:
            return -1
        else:
            return self.cir_queue[self.f_pointer]

    def Rear(self) -> int:
        if self.isEmpty() == True:
            return -1
        else:
            return self.cir_queue[self.r_pointer-1]
        
    def isEmpty(self) -> bool:
        if self.f_pointer == self.r_pointer and self.cir_queue[self.f_pointer] == None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.f_pointer == self.r_pointer and self.cir_queue[self.f_pointer] != None:
            return True
        else:
            return False


if __name__ == '__main__':
    cirQueue = MyCircularQueue(3)
    print(cirQueue.enQueue(1))
    print(cirQueue.enQueue(2))
    print(cirQueue.enQueue(3))
    print(cirQueue.enQueue(4))
    print(cirQueue.Rear())
    print(cirQueue.isFull())
    print(cirQueue.deQueue())
    print(cirQueue.enQueue(4))
    print(cirQueue.Rear())