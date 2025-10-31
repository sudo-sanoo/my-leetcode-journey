class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen=set()
        res=[]
        for num in nums:
            if num in seen:
                res.append(num)
            seen.add(num)

        return res
