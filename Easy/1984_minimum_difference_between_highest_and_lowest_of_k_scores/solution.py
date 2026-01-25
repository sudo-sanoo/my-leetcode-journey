class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1: return 0
        if n == k: return max(nums) - min(nums)
        
        nums = sorted(nums, reverse=True)

        res = float('inf')
        for i in range(n-k+1):
            x = nums[i] - nums[i+k-1]
            if x < res:
                res = x
            
        return res
