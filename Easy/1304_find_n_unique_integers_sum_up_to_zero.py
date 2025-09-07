class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        if n % 2 != 0:
            res.append(0)

        k = 1
        while len(res) < n: #can also use for i in range(1, n//2+1), this loop has less overhead
            res.append(k)
            res.append(-k)
            k+=1

        return res
