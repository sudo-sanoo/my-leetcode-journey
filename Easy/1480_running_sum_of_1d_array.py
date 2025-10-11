class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Memory Optimized attempt
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        return nums 

        '''
        # Initial attempt
        res = [nums[0]] * len(nums)

        x = nums[0]
        for i in range(len(nums)-1):
            x += nums[i+1]
            res[i+1] = x

        return res
        '''
