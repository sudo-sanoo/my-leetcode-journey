class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Two Pointers technique with O(n) time 
        arr = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(arr) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                arr[i] = nums[left] ** 2
                left += 1
            else:
                arr[i] = nums[right] ** 2
                right -= 1

        return arr
        

        '''
        # Square then Sort Approach
        # Runtime of O(nlogn)
        sq_nums = [i**2 for i in nums]

        return sorted(sq_nums)
        '''
