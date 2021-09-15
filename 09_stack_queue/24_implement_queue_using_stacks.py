'''
push(x)
pop()
peek()
empty()
'''

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.r_stack = [] # reversed
        self.queue = 0
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if x!= None:
            self.stack.append(x)
            self.queue += 1
        #self.stack.append(x) if x != None else null
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.empty():
            self.queue -= 1
            result = self.stack[0]
            self.stack = self.stack[1:]
            return result
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0] if not self.empty() else False
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.queue == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()