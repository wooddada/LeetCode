class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        sum_1= sum(costs)
        costs.sort(reverse=True)
        
        if coins>=sum_1:
            return len(costs)
        
        for i in range(len(costs)):
            sum_1 = sum_1-costs[i]
            if coins>=sum_1:
                return len(costs)-i-1