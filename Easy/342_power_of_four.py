class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 1

        while x < n:
            x *= 4
            
        return n == x
