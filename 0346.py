class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.window = [None] * size
        self.pointer = 0
        self.sum = 0
        self.count = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sum += val
        if self.window[self.pointer] is not None:
            self.sum -= self.window[self.pointer]
        self.window[self.pointer] = val
        self.pointer = (self.pointer + 1) % self.size
        if self.count < self.size:
            self.count += 1
        return 1.0 * self.sum / self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
