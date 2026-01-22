class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        res = 0
        zero_cnt = 0
        l = 0
        for r in range(n):
            if nums[r] == 0:
                zero_cnt += 1
            while zero_cnt > k:
                if nums[l] == 0:
                    zero_cnt -= 1
                l += 1
            res = max(r-l+1, res)

        return res
