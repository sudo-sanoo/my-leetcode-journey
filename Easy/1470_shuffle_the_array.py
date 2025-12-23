class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        numsX = [nums[i] for i in range(n)]
        numsY = [nums[i] for i in range(n, len(nums))]

        res=[]
        for x, y in zip(numsX, numsY):
            res.append(x) ; res.append(y)

        return res
