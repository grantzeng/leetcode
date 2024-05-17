class Solution:
    def maxProfit(self, prices: List[int]) -> int:



        """
            Idea:
            - Greedily try to lower buy price

            This works, but I'm not sure how to prove to you this algorithm is correct.

            Invariant you have to maintain is i <= j (can't buy in the future and sell now)
        """

        i, j = 0, 0 # buy and sell 

        profit = float('-inf')
        while j < len(prices):
            profit = max(prices[j] - prices[i], profit)
            if prices[j] <= prices[i]: 
                # Found a better buy price, greedily take it
                i = j 
            j += 1

        return profit      
            