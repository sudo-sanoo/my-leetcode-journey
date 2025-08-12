class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 1
        
        while x < n:
            x *= 3

        return x == n
