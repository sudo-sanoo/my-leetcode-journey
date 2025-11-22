class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt=0
        for n in nums:
            if n % 3 == 1:
                cnt += 1
            elif n % 3 == 2:
                cnt += 1
        return cnt
