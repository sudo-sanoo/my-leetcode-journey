class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Approach 2: Two Pointers
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
                continue
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1, j+1]

        return -1

        '''
        # Approach 1: HashMap
        numMap = {}

        for index, value in enumerate(numbers):
            if target - value not in numMap:
                numMap[value] = index
            else:
                return [numMap[target-value]+1, index+1]

        return -1
        '''
