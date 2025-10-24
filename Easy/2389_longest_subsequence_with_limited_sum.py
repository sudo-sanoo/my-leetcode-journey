class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        # More Runtime Efficient Approach
        nums.sort()
        for x in range(1, len(nums)):
            nums[x] += nums[x-1]
        nums.insert(0,0) # the "0" isn’t strictly required, it’s just a way to make the index = count of elements directly

        res = []
        for i in queries:
            l = 0
            r = len(nums) - 1 # r (right) is used to indirectly count the number of elements, instead of incrementing every time like in the initial solution

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= i:
                    l = mid + 1
                else:
                    r = mid - 1
            
            res.append(r) # if without nums.insert(0,0), this line here should be res.append(r+1)

        return res

        # # Initial Solution
        # nums = sorted(nums)
        # total = sum(nums)
        # answer = [0] * len(queries)

        # for i in range(len(queries)):
        #     if total < queries[i]:
        #         answer[i] += len(nums)
        #         continue

        #     x = 0
        #     for j in nums:
        #         x += j
        #         if x <= queries[i]:
        #             answer[i] += 1

        # return answer
