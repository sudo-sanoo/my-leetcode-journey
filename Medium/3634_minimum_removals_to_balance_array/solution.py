class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1: return 0
        nums.sort()
        # max <= min * k
        # return the number of removals
        sw = 0 # track the longest sliding window
        l = 0
        for r in range(1, n):
            while nums[r] > nums[l] * k:
                l+=1
            length = r-l+1
            if sw < length: 
                sw = length
        return n - sw
        
