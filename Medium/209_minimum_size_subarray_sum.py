class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0

        n=len(nums)
        min_cnt=len(nums)
        ps=0
        l=0
        for r in range(n):
            ps+=nums[r]
            while ps >= target:
                cnt=r-l+1
                min_cnt=min(min_cnt, cnt)
                ps-=nums[l]
                l+=1
                
        return min_cnt
