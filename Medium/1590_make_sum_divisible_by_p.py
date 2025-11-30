class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Mathematical proof:
        #   total_sum = sum(nums)
        #   sub_sum = ps[end] - ps[start] 
        #       (total_sum - sub_sum) % p == 0
        #       (total_sum % p) - (sub_sum) % p == 0
        #       total_sum % p == sub_sum % p
        #   total_sum % p == rem 
        #       rem == (ps[end] - ps[start]) % p
        #       ps[end] - ps[start] = rem % p
        #       ps[start] = (ps[end] - rem) % p 
        # Therefore, for each index [i], check if (ps[end] - rem) % p existed before
        modded = {0:-1} # Track ps[start] positions

        # If there exist a sub_sum == total_sum % p record the size of the subarray, then compare until we find the smallest size subarray

        total_sum = sum(nums)
        if total_sum % p == 0:
            return 0

        rem = total_sum % p
        res = float('inf')
        ps = 0 # subarray sum
        n = len(nums)

        for i in range(n):
            ps += nums[i]

            if (ps - rem) % p in modded:
                res = min(res, i - modded[(ps-rem)%p])

            modded[ps%p] = i

        return -1 if res == float('inf') or res == n else res
