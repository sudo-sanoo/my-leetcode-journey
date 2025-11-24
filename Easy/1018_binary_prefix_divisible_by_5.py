class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # optimized solution
        # time complexity of O(n)
        res=[]
        prefix = 0
        for bit in nums:
            prefix = (prefix << 1) | bit
            res.append(prefix % 5 == 0)

        return res
      
        # brute force solution
        # time complexity of O(n**2)
        res=[]
        bin_str = ""
        for i in range(len(nums)):
            bin_str += str(nums[i])
            res.append(int(bin_str, 2) % 5 == 0)

        return res
