import sys
class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words_dict = {}
        for index, word in enumerate(words):
            if word in self.words_dict:  # If key exists
                # Append list of indices
                self.words_dict[word].append(index)
            else:
                self.words_dict.update({word: [index]})

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Get the indices for both words
        word1_indices = self.words_dict[word1]
        word2_indices = self.words_dict[word2]

        # Return the minimum index difference between the two words
        min_distance = sys.maxsize
        for index1 in word1_indices:
            for index2 in word2_indices:
                min_distance = min(min_distance, abs(index1 - index2))
        return min_distance
