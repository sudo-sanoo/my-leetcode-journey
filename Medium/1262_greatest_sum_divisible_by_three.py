class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        rem1 = []
        rem2 = []
        for n in nums:
            total += n
            if n % 3 == 1:
                rem1.append(n)
            elif n % 3 == 2:
                rem2.append(n)

        if total % 3 == 0:
            return total

        rem1.sort()
        rem2.sort()

        if total % 3 == 1:
            remove_options = []
            if len(rem1) >= 1:
                remove_options.append(rem1[0])
            if len(rem2) >= 2:
                remove_options.append(rem2[0] + rem2[1])

            if not remove_options:
                return 0

            return total - min(remove_options)

        if total % 3 == 2:
            remove_options = []
            if len(rem2) >= 1:
                remove_options.append(rem2[0])
            if len(rem1) >= 2:
                remove_options.append(rem1[0] + rem1[1])

            if not remove_options:
                return 0

            return total - min(remove_options)
