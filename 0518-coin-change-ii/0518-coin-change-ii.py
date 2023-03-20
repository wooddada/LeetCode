class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
#        for i in range (len(coins)):
#            min_coins = coins[i]
#            min_coins = min(coins[i],min_coins)
#        rep = int(amount/min_coins) # 1 더해야되는지 유무 확인필요.
        dp = [0] * (amount + 1)
        dp[0] = 1
        coins = sorted(coins)
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = dp[j] + dp[j - coins[i]]
        return dp[amount]