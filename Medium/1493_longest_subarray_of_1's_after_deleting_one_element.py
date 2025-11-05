class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        if sum(nums) == n:
            return n-1

        l = 0
        maxRes = 0
        ps = 0
        for r in range(n):
            ps += nums[r]
            if ps <= (r-l)-1:
                ps -= nums[l]
                l += 1
            maxRes = max(maxRes, ps)

        return maxRes
