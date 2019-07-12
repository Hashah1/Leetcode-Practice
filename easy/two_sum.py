class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_freq_dict = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        freq = 1
        if number in self.num_freq_dict:
            freq += 1
        self.num_freq_dict.update({number: freq})

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if not self.num_freq_dict:
            return False
        for num in self.num_freq_dict: 
            if value - num in self.num_freq_dict:
                if value - num == num:
                    if self.num_freq_dict[value - num] > 1:
                        return True
                else:
                    return True
        return False