class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        if len(prices) > 1:
            for index in range((len(prices) - 1)):
                if prices[index] <= prices[index + 1]:
                    max_profit += prices[index + 1] - prices[index]
        return max_profit