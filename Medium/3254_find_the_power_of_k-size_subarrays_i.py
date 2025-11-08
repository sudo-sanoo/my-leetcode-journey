class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # Optimized Solution:
        if k == 1:
            return nums

        n = len(nums)
        res = []
        l = 0
        for r in range(1, n):
            if nums[r] != nums[r-1]+1:
                l = r
            if r >= k-1:
                if r-l+1 >= k:
                    res.append(nums[r])
                else:
                    res.append(-1)

        return res

        # # Brute force solution:
        # if k == 1:
        #     return nums

        # def findPower(i):
        #     for n in range(i, i+k-1):
        #         if nums[n]+1 == nums[n+1]:
        #             v = nums[n+1]
        #         else:
        #             return -1
        #     return v

        # res = []
        # for i in range(len(nums)-k+1):
        #     val = findPower(i)
        #     res.append(val)

        # return res
