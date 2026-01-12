class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [0]*nums.count(0) + [1]*nums.count(1) + [2]*nums.count(2)

        # zeros, ones, twos = nums.count(0), nums.count(1), nums.count(2)
        # for i in range(len(nums)):
        #     if zeros: 
        #         nums[i] = 0
        #         zeros -= 1
        #     elif ones: 
        #         nums[i] = 1
        #         ones -= 1
        #     else: 
        #         nums[i] = 2
        #         twos -= 1
