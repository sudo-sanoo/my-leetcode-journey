class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        start = 0
        end = len(letters)-1

        if letters[end] <= target:
            return letters[0]

        #Note: You can lexicographically compare strings directly, like lettters[0] >= "a"
        while start < end:
            mid = (start + end) // 2
            if letters[mid] > target:
                end = mid
            else:
                start = mid + 1

        return letters[start]
