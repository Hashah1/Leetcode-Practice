class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        length = len(flowerbed)
        if length is 1 and flowerbed[0] is 0:
            return True
        else:
            for pot_index in range(length):
                if pot_index is 0:  # Handle edge case
                    if flowerbed[pot_index] is 0 and flowerbed[pot_index + 1] is 0:
                        flowerbed[pot_index] = 1
                        count += 1
                elif pot_index == length - 1:
                    if flowerbed[pot_index] is 0 and flowerbed[pot_index - 1] is 0:
                        flowerbed[pot_index] = 1
                        count += 1
                else:
                    if flowerbed[pot_index] is 0 and flowerbed[pot_index + 1] is 0 and flowerbed[pot_index - 1] is 0:
                            flowerbed[pot_index] = 1
                            count += 1
                if count >= n:
                    return True
        return False