class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the sum from nums[0]..nums[curr-1] = nums[curr+1]..nums[len(nums)-1]
        res, ps, x = 0, 0, sum(nums)

        for i in range(len(nums)):
            if ps*2 == x:
                if nums[i] == 0:
                    res+=2
            if (ps*2)+1 == x or (ps*2)-1 == x:
                if nums[i] == 0:
                    res+=1
            
            ps+=nums[i]
        
        return res
