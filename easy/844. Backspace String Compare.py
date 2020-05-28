class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        """TC: O(len(S) + len(T)), SC: O(1)"""
        s_idx = len(S)
        t_idx = len(T)
        # Iterate while both ptrs are valid
        while s_idx >= 0 and t_idx >= 0:
            # Start off with a backspace of 1 since we start outside str.
            backspaces = 1
            while backspaces > 0:
                s_idx -= 1
                # If we hit a backspace, increment counter
                if s_idx >= 0 and S[s_idx] == "#":
                    backspaces += 1
                else: # Decrement counter as a 'skip'
                    backspaces -= 1
            # Repeat for string T
            backspaces = 1
            while backspaces > 0:
                t_idx -= 1
                if t_idx >= 0 and T[t_idx] == "#":
                    backspaces += 1
                else:
                    backspaces -= 1
            # If ptrs are valid, return false if different char after all possible skips
            if s_idx >= 0 and t_idx >= 0 and S[s_idx] != T[t_idx]:
                return False
        # Return true if both ptrs have finished string processing.
        return s_idx < 0 and t_idx < 0