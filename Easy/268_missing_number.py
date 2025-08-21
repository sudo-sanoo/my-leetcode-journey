class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in nums:
            if i+1 not in nums and i+1 == len(nums):
                return i+1
            elif i-1 not in nums and i-1 >= 0:
                return i-1
            else:
                continue

        return -1
