class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range (n+1)]
        
        for i in range(1, n+1):
            for j in range (1, int(i**(0.5))+1):
#                if j**2>n :
#                    continue
                dp[i] = min(dp[i], dp[i-j**2]+1)
        return dp[n]