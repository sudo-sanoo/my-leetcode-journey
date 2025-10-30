class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        res=0
        cnt=0
        l=0
        tmp=nums[1]-nums[0]
        for r in range(1,len(nums)):
            x = nums[r] - nums[r-1]
            if tmp == x:
                if (r-l)+1 >= 3:
                    cnt+=1
                    res+=cnt
            else:
                l=r-1
                cnt=0
                
            tmp=x

        return res
