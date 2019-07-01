class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        left = right = max_size = 0
        
        while right < len(s):
            # If item isnt in set
            if s[right] not in seen:
                # Update max, enlarge the window
                seen.add(s[right])
                right += 1
                window_size = right - left
                max_size = max(max_size, window_size)
            else:
                # Otherwise, remove from set, increment the left index
                # and increment max_size
                seen.remove(s[left])
                left += 1
        print(max_size)
        return max_size

        # seen = {}
        # start_index = stop_index = max_size = 0
        # for each_char in enumerate(s):
        #     char = each_char[1]
        #     char_index = each_char[0]
        #     # Add the char and its index to the dictionary.
        #     if char in seen:
        #         # Update the start index by the index at which
        #         # the element was seen at in the dictionary
        #         start_index = max(start_index,seen[stop_index] + 1)
        #     stop_index += 1
        #     seen.update({char: char_index})
        #     max_size = max(max_size, stop_index - start_index + 1)

        # return max_size
                
if __name__ == "__main__":
    a = Solution()
    a.lengthOfLongestSubstring("pwwke")
    