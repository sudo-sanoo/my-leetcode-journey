class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 3 indices, i, j and k where k is the pivot index
        # return the pivot index, where sum(i to k-1) == sum(k+1 to j) else -1
        # sum(i to k-1) can be represented as "left"
        # sum(k+1 to j) can be represented as "right"
        # left = ps[k-1] - ps[i]
        # right = ps[j] - ps[k+1]

        # Optimized approach
        left, right = 0, 0

        for j in nums:
            right += j

        for i in range(len(nums)):
            left += nums[i-1] if i - 1 >= 0 else 0
            right -= nums[i]
            if left == right:
                return i

        return -1

        '''
        # Initial approach
        ps = 0
        for k in range(len(nums)):
            rnums = nums[k:]
            if sum(rnums) - nums[k] == ps:
                return k

            ps += nums[k]

        return -1
        '''
