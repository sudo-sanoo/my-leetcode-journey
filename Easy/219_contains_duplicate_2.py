class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashSet = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                hashSet.remove(nums[left])
                left += 1
            if nums[right] in hashSet:
                return True
            hashSet.add(nums[right])

        return False
        
        '''
        # Runtime Complexity: O(n**2)
        # Brute force approach

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True

        return False
        '''
