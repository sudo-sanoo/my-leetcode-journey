# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return n
            
        start = 0
        
        while start < n:
            mid = (start + n) // 2
            if isBadVersion(mid):
                n = mid
            else:
                start = mid + 1

        return start
