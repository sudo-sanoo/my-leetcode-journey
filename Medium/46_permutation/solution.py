class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # so in this problem we can make an imaginary tree to visualize all possible solutions
        # lets say nums = [1,2,3]
        #   if we pick [1], 
        #   we can make a branch where the next number we can pick is [2,3],
        #   then we pick [2],
        #   we can make another branch where the next number left is [3]
        # visualize this selection of numbers as a tree:
        #   [1] -> [1,2] -> [1,2,3]
        # and we have a tree with one branch, where the end of this branch is one of the answer

        # we can then perform DFS (Depth-First Search) on this imaginary tree to
        # explore each branch as deeply as possible before BACKTRACKING to the next branch

        if len(nums) <= 1:
            return [nums]

        n = len(nums)
        res = []
        permutation = []

        def backtrack():
            if len(permutation) == n:
                res.append(permutation[:])
                return
                
            for x in nums:
                if x not in permutation:
                    permutation.append(x)
                    backtrack()
                    permutation.pop()

        backtrack()
        return res
