class Solution(object):
    def isPowerOfTwo(self, n):
        x = 1

        while x < n:
            x *= 2 

        return x == n
