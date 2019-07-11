class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_stk = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.max_stk.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.max_stk.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.max_stk[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.max_stk)
        

    def popMax(self):
        """
        :rtype: int
        """
        max_val = self.max_stk[0]
        index = 0
        for i,each in enumerate(self.max_stk):
            if each >= max_val:
                max_val = each
                index = i
        del self.max_stk[index]
        return max_val

# Your MaxStack object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MaxStack()
    obj.push(5)
    obj.push(1)
    # obj.push(5)
    # top1 = obj.top()
    topmax = obj.popMax()
    # top2 = obj.top()
    peekmax = obj.peekMax()
    pass
    # pop = obj.pop()
    # top3 = obj.top()
