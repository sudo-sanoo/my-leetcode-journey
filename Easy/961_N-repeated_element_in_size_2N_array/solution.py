class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            if num in numSet:
                return num
            numSet.add(num)
        return -1
