class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Improved Solution
        n = len(nums) # ranges of number supposed to be in the list
        total = n * (n + 1) // 2 # supposed sum if all the list of numbers are complete with no missing number
        return total - sum(nums) # supposed sum - current sum will get the answer

        '''
        for i in nums:
            if i+1 not in nums and i+1 == len(nums):
                return i+1
            elif i-1 not in nums and i-1 >= 0:
                return i-1
            else:
                continue

        return -1
        '''
