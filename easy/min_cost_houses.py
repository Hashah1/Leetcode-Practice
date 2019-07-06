class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        prev_cost_red = prev_cost_blue = prev_cost_green = 0
        for each_house in costs:
            # Get the minimum cost to paint each color
            # Each color cost is the sum of either of the previous two colors 
            # (since no adj allowed) with the current color of its kind
            min_cost_red =  min(prev_cost_blue, prev_cost_green) + each_house[0]          
            min_cost_blue = min(prev_cost_red, prev_cost_green) + each_house[1]
            min_cost_green = min(prev_cost_red, prev_cost_blue) + each_house[2]
            # Store record of each color.
            prev_cost_red = min_cost_red
            prev_cost_blue = min_cost_blue
            prev_cost_green = min_cost_green
        
        return min(min_cost_red,min_cost_blue,min_cost_green)

  

if __name__ == "__main__":
    a = Solution()
    a.minCost([[17,2,17],[16,16,5],[14,3,19]])