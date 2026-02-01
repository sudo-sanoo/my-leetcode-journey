class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 3: return sum(nums)
        
        sorted_nums = sorted(nums[1:])
        
        return nums[0] + sorted_nums[0] + sorted_nums[1]
