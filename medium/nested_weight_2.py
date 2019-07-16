# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def __init__(self):
        self.height = 1
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        height = self.get_depth(nestedList, 1)
        return self.get_nested_sum(nestedList, height)

    def get_depth(self, nestedList, depth):
        self.height = max(depth,self.height)  # Get max depth
        for each_list in nestedList:
            # If dealing with list, recurse and pass new depth
            if each_list.getList():
                self.height = self.get_depth(each_list.getList(), depth + 1)
        return self.height

    def get_nested_sum(self, nestedList, height):
        s = 0
        # Loop through all items in nested lists
        for each_list in nestedList:
            # If item is an integer, get sum
            if each_list.getInteger():
                s += each_list.getInteger() * height
            else: 
                # Recurse and DECREMENT depth/height
                s += self.get_nested_sum(each_list.getList(), height - 1)
        return s