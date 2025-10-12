class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # ps[i] = sum of nums[0..i]
        # sum(i,j) = ps[j] - ps[i-1]
        # k = ps[j] - ps[i-1]
        # ps[i-1] = ps[j] - k
        # if (current prefix sum, ps[j] - k) = (some previous prefix sum, ps[i-1]), then a subarray exists between i and j, where sum of i to j will be k

        res = 0
        ps = 0
        ps_map = {0: 1}

        for i in nums:
            ps += i

            if ps - k in ps_map:
                res += ps_map[ps - k]

            ps_map[ps] = ps_map.get(ps, 0) + 1

        return res
