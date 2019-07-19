class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Use two arrays, which will always have the same
        # length and will have a one-one relationship
        self.hashmap = []
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        # Update the hashashmapap
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                self.hashmap[i] = [key,value]
                return
        # Add to hashmap if none found
        self.hashmap.append([key,value])
            

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        # Check if key is in list, return false otherwise
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                return self.hashmap[i][1]
        return -1
        


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        # Check if key is in list, return false otherwise
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                del self.hashmap[i]
        return -1
        


if __name__ == "__main__":
    a = MyHashMap()
    a.put(1,1)
    a.put(2,2)
    ans = a.get(1)
    ans = a.get(3)
    a.put(2,1)
    ans = a.get(2)
    a.remove(2)
    ans = a.get(2)