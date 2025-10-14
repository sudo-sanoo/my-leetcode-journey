class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # this question requires the "Hashmap Prefix" trick, like LeetCode 560: Subarray Sum Equals K

        # two indices traverse nums, i and j
        # sum(i, j) = ps[j] - ps[i-1]
        # for this question sum(i, j) needs to be a multiple of k
        # (ps[j] - ps[i-1]) % k == 0
        # ps[j] % k == ps[i-1] % k 
        # Store remainders in a hashmap, return True if the same remainder is seen again after 2 iterations
        ps = 0
        r_map = {ps: -1} # stores the prefix sums modulo k encountered so far with its index

        for i in range(len(nums)):
            ps += nums[i]

            r = ps % k
            if r in r_map:
                if i - r_map[r] >= 2:
                    return True
            else:
                r_map[r] = i

        return False
