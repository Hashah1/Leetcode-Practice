class WordDictionary:
    """
    Strategy:
    Use dict
    O(1) access and O(1) lookup
    1.When adding:
        Store len(word) -> All words under that length
        O(1)
    2.When searching:
        Get list of all words under that length
        Iterate over each word, and check char with the target word. Return true if match.
        O(len(search_word^2))

    Better option:
    Trie
    -> Time Complexity: addition: O(2^h), search: O(2^h), h - height -- Updated with correct complexity!
    -> Space Complexity: O(2^h), h = height -- Updated with correct complexity!
    """

    class Node():
        def __init__(self):
            self.mapping = {}
            # self.num_chars_left = 0
            self.is_word_complete = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur_node = self.root
        self.insertion_helper(word, cur_node)

    def insertion_helper(self, word, cur_node):
        # Create new node for addition.
        new_node = self.Node()
        # Finished adding a word
        if not word:
            cur_node.is_word_complete = True
            return
        beg_char = word[0]
        # Check if the first character of the word is in the current node's mapping
        if beg_char in cur_node.mapping:
            # Just move to the next node.
            cur_node = cur_node.mapping[beg_char]
        # If the char is not in the current mapping, insert into the current mapping with the words left
        else:
            # Each char will have a pointer to rest of the nodes.
            cur_node.mapping[beg_char] = new_node
            # Advance to the new node
            cur_node = new_node
        return self.insertion_helper(word[1:], cur_node)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        cur_node = self.root
        return self.word_finder(word, cur_node)

    def word_finder(self, word, cur_node):
        if not word:
            if cur_node.is_word_complete: # Ending of search
                return True
            return False

        beg_char = word[0]
        # If char is not a wildcard
        if beg_char != ".":
            if beg_char in cur_node.mapping:
                cur_node = cur_node.mapping[beg_char]
                return self.word_finder(word[1:], cur_node)
        elif beg_char == ".":
            # If a wildcard is encountered, test all potential keys in mapping
            for cur_char, next_node in cur_node.mapping.items():
                is_word_found = self.word_finder(word[1:], next_node)
                if is_word_found:
                    return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
