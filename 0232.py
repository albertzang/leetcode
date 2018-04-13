class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.stack_in = deque()
        self.stack_out = deque()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while len(self.stack_out):
            self.stack_in.append(self.stack_out.pop())
        self.stack_in.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.stack_in):
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while len(self.stack_in):
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not (len(self.stack_in) + len(self.stack_out))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
