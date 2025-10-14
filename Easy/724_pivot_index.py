class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 3 indices, i, j and k where k is the pivot index
        # return the pivot index, where sum(i to k-1) == sum(k+1 to j) else -1
        # sum(i to k-1) = ps[k-1] - ps[i]
        # sum(k+1 to j) = ps[j] - ps[k+1]

        # Optimized approach
        left, right = 0, 0

        for i in nums:
            right += i

        for j in range(len(nums)):
            left += nums[j-1] if j - 1 >= 0 else 0
            right -= nums[j]
            if left == right:
                return j

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
