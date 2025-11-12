import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for n in nums:
            if n == 1:
                cnt += 1
        if cnt:
            return len(nums) - cnt

        min_sub_len = float("inf")

        for l in range(len(nums)):
            cur_gcd = 0
            for r in range(l, len(nums)):
                if r-l+1 >= min_sub_len:
                    break
                cur_gcd = math.gcd(cur_gcd, nums[r])
                if cur_gcd == 1:
                    min_sub_len = r-l+1
                    break

        if min_sub_len == float("inf"):
            return -1

        return (min_sub_len - 1) + len(nums) - 1
