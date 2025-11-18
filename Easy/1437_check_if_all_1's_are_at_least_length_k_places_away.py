class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist_map = defaultdict()

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if nums[i] in dist_map:
                if ((i - dist_map[nums[i]])-1) < k:
                    return False
            dist_map[nums[i]] = i

        return True
