class Solution(object):
    def hasZero(self, num):
        return "0" in str(num)
    
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []

        k = 1
        while sum(res) < n:
            if self.hasZero(k) or self.hasZero(n-1):
                k += 1
                n -= 1
                continue

            res.append(k)
            res.append(n-1)

        return res
