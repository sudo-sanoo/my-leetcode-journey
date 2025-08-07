# When the time complexity required is O(log n), the clue here is to use binary search algorithm
# The key here is to find the target and return the index when it is in the list.
# But what if the target is not in the list?
# We don't have to insert the value, but rather to intuitively return the index of where it could be if target was inserted in the list in ascending order
# By return left, we can always return tbe index of the target if it is not in the list
# If target is smaller than the left-most integer in a sorted list, when the loop ends, it will end at the first integer in the list. By returning "left", we can return the first index at 0, which is also where it would be inserted
# If target is larger than the right-most integer in a sorted list, when the loop ends, it will end at the final integer in the list. By returning "left", we also effectively return the index of the final index, which is also where it would be inserted

# Runtime Complexity: O(log n)

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return left
        
