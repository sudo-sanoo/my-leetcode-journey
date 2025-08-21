class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # An in-place algorithm modifies the array directly without creating another full copy.
        # It may still use a small, constant amount of extra memory (e.g., variables or pointers).
        # Improved Approach: Using "k" as a comparative that keeps being updated, and "i" to traverse the list
        #    - No need for removing elements or keeping track of the length of the list
        #    - If compared is not equal, then it should be in the list, if not, then it does not belong there
        #    - "k" is used as a count of how many elements should be in the list
        #    - Runtime Complexity: O(n)
        if len(nums) == 0:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1

        return k

        '''
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
        '''
