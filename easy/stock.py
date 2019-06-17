def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_val = max_val = prices[0]
        profit = 0
        
        # for every element after first one
        for val in prices[1:]:
            # If lesser than min, update both values
            if val < min_val:
                min_val = val
                max_val = val
            # Update max and compare the diff of max/min and profit
            elif val > max_val:
                max_val = val
                profit = max(profit, max_val-min_val)
        return profit