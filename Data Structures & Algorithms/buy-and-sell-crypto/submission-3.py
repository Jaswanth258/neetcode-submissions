class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        current = prices[0]

        for price in prices[1:]:
            if price < current:
                current = price

            profit = price - current
            res = max(res , profit)    
        
        return res
            
