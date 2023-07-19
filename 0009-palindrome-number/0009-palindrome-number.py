class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        if x ==0 or len(str(x))==1:
            return True
        a = str(x)
        for i in range(len(a)//2):
            if a[i] !=a[len(a)-1-i]:
                return False
        else :
            return True