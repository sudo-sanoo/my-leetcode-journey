class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach: Boyer-Moore's Majority Vote Algorithm
        # This algorithm loops through the array only once
        #   1. Keeps 2 possible candidates and their count (numbers are fighting for the 2 spots)
        #       - "count" is here to determine which 2 candidates are selected  
        #   2.After iterating through the array, verify the number 
        # Always return the candidate that is not None (null), that its count is not 0
        if not nums:
            return []
        
        # Step 1: Find possible candidates
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        #Step 2: Verify the conditions
        result = []
        for candidate in (candidate1, candidate2):
            if candidate is not None and nums.count(candidate) > len(nums)//3:
                result.append(candidate)

        return result
