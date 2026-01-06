class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sum of 3 distinct indexed integers have to be equal to 0
        # 3 distinct indexed integers equal to 0 is one triplet
        # there can be more than one triplets
        # return all the triplets

        n = len(nums)
        nums.sort()
        res = []

        for i in range(n-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = n-1
            # find two numbers that equal to (-nums[i])
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
