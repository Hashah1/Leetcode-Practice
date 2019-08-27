import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] is 1:
                return idx
        return -1
