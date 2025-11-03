class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution: Prefix Sum
        minSum = maxSum = ps = 0
        for i in nums:
            ps += i
            if ps < minSum:
                minSum = ps
            if ps > maxSum:
                maxSum = ps
        
        return maxSum - minSum

        # Solution: Kadane's Algorithm
        currentMax = 0
        maxSum = nums[0]
        currentMin = 0
        minSum = nums[0]

        for i in nums:
            currentMax = max(currentMax, 0)
            currentMax += i
            maxSum = max(currentMax, maxSum)

        for j in nums:
            currentMin = min(currentMin, 0)
            currentMin += j
            minSum = min(currentMin, minSum)

        if abs(minSum) > maxSum:
            res = abs(minSum)
        else:
            res = maxSum

        return res
