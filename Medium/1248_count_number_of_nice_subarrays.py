class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        for i in range(len(nums)): # to ignore even numbers and count the number of odds
            if nums[i] % 2 != 0:
                nums[i] = 1
            else:
                nums[i] = 0

        ps, res = 0, 0
        ps_map={0:1} # ps_map to store all prefix sum that has existed
        for i in nums:
            ps+=i
            if ps-k in ps_map: # ps-k check if there are k amount of odd nums, from the previous k odd nums
                res+=ps_map[ps-k]
            ps_map[ps] = ps_map.get(ps,0)+1

        return res
