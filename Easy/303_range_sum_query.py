class NumArray(object):
    
    # Memory-optimized attempt:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        x = 0

        for i in self.nums[left:right+1]:
            x += i

        return x

    '''
    # Runtime-optimized attempt:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ps = [0] * len(nums)
        if nums:
            self.ps[0] = nums[0]
            for i in range(1, len(nums)):
                self.ps[i] = self.ps[i-1] + nums[i]
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.ps[right]
        # total(low, high) = ps[high] - ps[left-1]
        return self.ps[right] - self.ps[left-1]
    '''

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
