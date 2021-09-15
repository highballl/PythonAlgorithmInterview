class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None]*self.k
        self.front = -1
        self.rear = 0


    def enQueue(self, value: int):
        if not self.isFull():
            self.rear = (self.rear+1) % self.k
            self.queue[self.rear] = value
            #self.queue.append(value)
            return True
        else:
            return False

    def deQueue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % self.k
            #return self.queue[self.front]
            #self.queue.pop()
            return True
        else:
            return False

    def Front(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]

    def Rear(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[(self.front+1)%self.k]
            #return self.queue[-1]

    def isEmpty(self):
        if self.front == self.rear:
        #if len(self.queue) == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.front == (self.rear+1)%self.k:
        #if len(self.queue) == self.k:
            return True
        else:
            return False

    '''
    def clear(self):
        self.front = self.rear
    '''