"""
704. Binary Search
https://leetcode.com/problems/binary-search/

Time: O(log n)
Space: O(1)
"""

class Solution(object):

    def search(self, nums, target):

        low = 0 #first index in the list 
        high = len(nums) - 1 #last index in the list 

        while low <= high: #iterate the whole list until there is no more
            mid = (low + high) // 2 #assign a medium value 

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1 #eliminate the left half (lesser values in a sorted array)
            else:
                high = mid - 1 #eliminate the right half (greater values in a sorted array)

        return -1
