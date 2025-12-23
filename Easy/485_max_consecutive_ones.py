class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        maxRes = 0
        for n in nums:
            if n == 1:
                res += 1
            else:
                res = 0

            maxRes = max(maxRes, res)

        return maxRes
