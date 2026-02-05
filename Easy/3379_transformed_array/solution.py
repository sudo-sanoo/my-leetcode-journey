class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        # optimized solution in cpp
        res = []
        n = len(nums)
        for i in range(n):
            if nums[i] == 0: res.append(nums[i])
            elif nums[i] < 0: 
                idx = i - abs(nums[i])
                while idx < 0:
                    idx += n
                res.append(nums[idx])
            else: 
                idx = i + nums[i]
                while idx > n-1:
                    idx -= n
                res.append(nums[idx])
        return res
