class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = 0
        r = len(nums)-1
        res = 0
        while l<r:
            x = nums[l]+nums[r]
            if x > res:
                res = x
            l += 1
            r -= 1
        return res
