class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # Optimized Solution
        if sum(nums) % 2: # if sum(nums) % 2 is 1, meaning there can be no equal 2 partitions
            return 0
        return len(nums)-1

        # Brute-force Solution
        total = sum(nums)
        cnt = 0
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

            if ((total-nums[i]) - nums[i]) % 2 == 0:
                cnt += 1

        return cnt 
