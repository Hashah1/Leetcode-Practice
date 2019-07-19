class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        iso_dict = {}
        for char_index in range(len(s)):
            if s[char_index] in iso_dict:
                if iso_dict[s[char_index]] != t[char_index]:
                    return False
            elif t[char_index] in iso_dict.values():
                for k,v in iso_dict.items():
                    if v == t[char_index] and k != s[char_index]:
                        return False
            iso_dict.update({s[char_index]:t[char_index]})
        return True