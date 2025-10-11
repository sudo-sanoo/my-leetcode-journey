class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res[i] = product of all elements in nums, except nums[i]
        # This can be broken down into two parts, "everything before i" and "everything after i"
        
        # res[i] = (everything before i) * (everything after i) with the mathematical expression below:
        # res[i] = (nums[0] * nums[1] * ... * nums[i-1]) * (nums[i+1] * nums[i+2] * ... * nums[n-1])
        # Simplify that, we get:
        # res[i] = prefix[i] * suffix[i]

        # To get the suffix

        res = [1] * len(nums) # define the size of res to be equal the size of nums first

        # Each prefix[i] = product of everything BEFORE i
        # For example, using Testcase #1:
        # prefix[0] = 1 (nothing before nums[0])
        # prefix[1] = 1 * 1
        # prefix[2] = 1 * 1 * 2
        # prefix[3] = 1 * 1 * 2 * 3
        # So we get prefix = [1, 1, 2, 6]

        # Optimized code (update res along "x")         # Initial code (get x, and append one by one)
        # -------------------------------------         # --------------------------------------------
        prefix = 1                                      # prefix = []
                                                        # x = 1
        for i in range(len(nums)):                      # for i in range(len(nums)):
            res[i] = prefix                             #     prefix.append(x)
            prefix *= nums[i]                           #     x *= nums[i]

        # Each suffix[i] = product of everything AFTER i
        # For example, using Testcase #1:
        # suffix[0] = 2 * 3 * 4
        # suffix[1] = 3 * 4
        # suffix[2] = 4
        # suffix[3] = 1 (nothing after nums[3])
        # So we get suffix = [24, 12, 4, 1]

        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
