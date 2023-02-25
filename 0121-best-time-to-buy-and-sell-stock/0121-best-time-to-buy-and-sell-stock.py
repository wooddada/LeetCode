class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        price_min=10000
        profit_max = 0
        for price in prices:
            price_min = min(price,price_min)

            profit_max = max(price-price_min, profit_max)
        
        return profit_max