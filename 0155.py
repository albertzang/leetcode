class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_stack = list()
        self.min = float('inf')


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if x < self.min:
            self.min = x
        self.min_stack.append(self.min)


    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        self.min = self.getMin()
        if self.min is None:
            self.min = float('inf')


    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        return None


    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]
        return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
