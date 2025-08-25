# What is Dynamic Programming (DP)?
#   - Dynamic Programming is an algorithmic technique for solving complex problems by breaking it down to smaller, overlapping subproblems.
#   - The core idea is to solve each subproblem only once and store its solution, typically in a table or array to avoid redundant computation when the subproblem is encountered again

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach: Kadane's Algorithm
        # Kadane's Algorithm is a dynamic programming algorithm used to find the find the maximum sum of a contiguous subarray within a one-dimensional array of numbers
        # The idea of this algorithm is to iterate through the array, keeping track of:
        #   - Current Sum of numbers (current sum of the iteration)
        #   - Maximum Sum or Global Sum of numbers (largest sum in the array)
        # How Kadane's Algorithm works is that it iterates through the array of numbers, when encountering a negative integer, avoid the negative number as it only makes the "Sum" smaller
        # If the sum of a subarray is negative, discard the sum, as it cannot be the largest when there are positive integers in the array 
        # Steps:
        #   1. Kadane's Algorithm runs one loop
        #   2. Keep track of the currentSum by adding the current element to it
        #   3. Before adding the current element, check if currentSum is negative, if it is, reset it to zero
        #   4. Initialize maxSum as the first element in the array, ensures always starting at a valid subarray num, even if all numbers are negative
        #   5. Update maxSum by comparing it with the currentSum and the maxSum so far
        
        currentSum = 0
        maxSum = nums[0] #Process 4
        
        for i in nums: #Process 1. The whole loop only runs once with no repeat.
            currentSum = max(currentSum, 0) #Process 3
            currentSum += i #Process 2
            maxSum = max(currentSum, maxSum) #Process 5

        return maxSum 
