class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # An in-place algorithm modifies the array directly without creating another full copy.
        # It may still use a small, constant amount of extra memory (e.g., variables or pointers).
        # Improved Approach:
        # (solution in progress)
        
        # Approach 1: Brute-force, uneccessary .remove() and while loop worse case having to loop n times.
        #    - Runtime Complexity of O(n**2)
        result = len(nums)
        base = 0
        compare = 1

        while compare < result:
            if nums[base] == nums[compare]:
                nums.remove(nums[compare])
                result -= 1
            else:
                base += 1
                compare += 1

        return result
