class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = 1
        summ = 0

        for i in str(n):
            i = int(i)
            product *= i
            summ += i   

        return product - summ
