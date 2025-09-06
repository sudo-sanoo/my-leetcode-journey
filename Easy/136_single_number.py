class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime Complexity of O(n**2)
        # Iterating through every num and count by re-iterating through the list is n*n
        for num in nums:
            if nums.count(num) == 1:
                return num

        return -1
