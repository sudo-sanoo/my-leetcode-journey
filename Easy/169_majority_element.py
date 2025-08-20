class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numHash = {}

        if len(nums) == 1:
            return nums[0]

        for i in nums:
            if i not in numHash:
                numHash[i] = 1
            else:
                numHash[i] += 1
                if numHash[i] > len(nums)/2:
                    return i
