class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        """
        Thought process:
        TC: O(len(s)), SC: O(number of substrings under criteria)

        Have a hashmap: valid_substr -> occurrences
        Loop:start from idx 0
            - Check all substrings from size minsize to maxsize
            - Convert the substring to a set, and check its length against max_unique_letters
        """
        def is_uniqueness_valid(substr):
            return len(set(substr)) <= maxLetters

        mapping = defaultdict()
        for idx in range(len(s) - minSize + 1):

            # Grab substr of len minSize
            min_substr = s[idx:idx + minSize]

            # Grab substr of len maxSize if possible
            if idx + maxSize < len(s):
                max_substr = s[idx:idx + maxSize]
            else:
                max_substr = None

            # Convert both to sets. Check if <= maxLetters
            if max_substr and is_uniqueness_valid(max_substr):
                if max_substr in mapping:
                    mapping[max_substr] += 1
                else:
                    mapping[max_substr] = 1
            # If so, add to mapping
            if min_substr != max_substr and is_uniqueness_valid(min_substr):
                if min_substr in mapping:
                    mapping[min_substr] += 1
                else:
                    mapping[min_substr] = 1
        # Get the maximum occurrence
        max_occ = 0
        for v in mapping.values():
            max_occ = max(max_occ, v)
        return max_occ
