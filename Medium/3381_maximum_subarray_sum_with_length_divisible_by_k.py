class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefixSum = 0
        # On a 32-bit system, sys.maxsize is typically 2**31 - 1 or 2,147,483,647
        #   The minimum value (using two's complement representation) is -sys.maxsize - 1
        # On a 64-bit system, sys.maxsize is typically 2**63 - 1 or 9,223,372,036,854,775,807
        #    The minimum value is -sys.maxsize - 1
        maxSum = -sys.maxsize # represent the minimum practical integer value
        kSum = [sys.maxsize // 2] * k
        kSum[k - 1] = 0
        for i in range(n):
            prefixSum += nums[i]
            maxSum = max(maxSum, prefixSum - kSum[i % k])
            kSum[i % k] = min(kSum[i % k], prefixSum)

        return maxSum
