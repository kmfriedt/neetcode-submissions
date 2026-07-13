class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        # if there is no second day then return 0
        if len(prices) == 1:
            return 0

        max_profit = 0
        
        max_price = 0
        l, r = 0, 1
        


        # prices = [10, 1, 5, 6, 7, 1]
        #            0  1  2  3  4  5  6  7  8         
        # prices = [10, 3, 5, 6, 7, 1, 3, 6, 7]
        #               l           r        r
        """
         0  1  2  3  4  5  6   len = 7  len-1 = 6
        [2, 1, 2, 1, 0, 1, 2]
                     l     r     
        """

        # ideal is buy at 1 sell at 7 profit = 6
        # how do we do that?
        # basically have a window in which we buy the stock

        # start at 10 and 1, 1 is less than 10 so move ahead to 1, 5
        # 5 is more than 1 move second pointer ahead while the next item is greater 
        # once it is not then we record the max profit

        # only update the min_price if we see a smaller one

        # set up the starting point
        while l < len(prices) - 1 and prices[r] < prices[l]:
            l += 1
            r += 1
        print(f"{l}, {r}")
        min_price = prices[l] # what we buy at
        while r < len(prices):
            # find the higest price in the window
            while r < len(prices) - 1 and prices[r+1] > prices[r]:
                r  += 1
            max_profit = max(max_profit, prices[r] - min_price)
            print(f"max profit: {max_profit}, l:{l}, r:{r}")
            r += 1
            if r < len(prices) and prices[r] < min_price:
                l = r
                min_price = prices[l]
                r += 1

        return max_profit