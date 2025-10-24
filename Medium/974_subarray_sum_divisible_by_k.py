class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Prefix sum, ps is used here to avoid O(n^2) operations
        # If the (current prefix sum - previous prefix sum) % k == 0, then condition is met, so
        #   mathematically, (current ps % k) - (previous ps % k) == 0
        #   if simplified,  (current ps % k) = (previous ps % k) 
        # So, if the current prefix sum modulo k == previous prefix sum modulo k, then res += (previous counts)
        # Idea: ps % k = (ps % k that has already existed), increase res
        res = 0
        ps = 0
        r_map = {0: 1} # stores the prefix sums modulo k (store remainder)
        
        for i in nums:
            ps += i
            r = ps % k
            
            if r in r_map:
                res += r_map[r] # (combinatorics addition)
                # r_map[r] counts how many prefix sums had the same remainder before, each one forms a valid subarray with the current index

            r_map[r] = r_map.get(r, 0) + 1

        return res
        
        # # Brute-force Approach
        # res = 0
        # for i in range(len(nums)):
        #     x = 0

        #     for j in range(i, len(nums)):
        #         x += nums[j]

        #         if x % k == 0:
        #             res += 1

        # return res
