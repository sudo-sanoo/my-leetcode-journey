class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # Time Complexity: O(N∗K∗Log(K))
        # Space Complexity: O(N) 
        def getXSum(i):
            occurence = {}
            ps = 0
            for r in xrange(i, i+k):
                occurence[nums[r]] = occurence.get(nums[r], 0) + 1
                ps += nums[r]

            if k == x:
                return ps

            sorted_occurences = sorted(
                occurence.items(),
                key=lambda item: (item[1], item[0]), 
                reverse = True
            )
            
            xs = 0
            for num, occ in sorted_occurences[:x]:
                xs += (num * occ)

            return xs

        answer = []
        ansLength = len(nums)-k+1
        for i in range(ansLength):
            res = getXSum(i)
            answer.append(res)

        return answer
