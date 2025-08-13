class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        #Approach 1: Using String
        #Time Complexity: O(log n)
        strNum = str(num)

        while num > 9:
            num = sum(int(digit) for digit in strNum)
            strNum = str(num)

        return num
