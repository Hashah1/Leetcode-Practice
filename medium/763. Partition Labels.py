class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # TC = O(len(S)), SC = O(1)
        left_bound = 0
        right_bound = 0
        map_char_to_idx = {char: idx for idx, char in enumerate(S)}
        res = []
        for idx, char in enumerate(S):
            # Get the last seen index of the current char
            last_seen = map_char_to_idx[char]
            # Update right bound if last seen index is greater than current right bound.
            right_bound = max(last_seen, right_bound)
            if idx == right_bound:
                # Reached the last element of current partition
                # Mark the length via left bound
                res.append(right_bound - left_bound + 1)
                left_bound = right_bound + 1
        return resgit