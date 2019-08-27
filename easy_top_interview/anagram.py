import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        return False if count_s != count_t else True
