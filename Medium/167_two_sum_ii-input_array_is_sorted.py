class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}

        for index, value in enumerate(numbers):
            if target - value not in numMap:
                numMap[value] = index
            else:
                return [numMap[target-value]+1, index+1]

        return -1
