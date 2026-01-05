class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # im pretty sure to get the absolute max, there are two scenarios:
        #   1. if there is an even number of negatives, we can turn every negatives to positive
        #   2. if there is an odd number of negatives,
        #       find minimum absolute value in the entire matrix,
        #       then take the entire sum of the matrix, and sum - 2*(minimum absolute value)

        res = 0
        minimumAbsoluteValue = float('inf')
        negativeCount = 0
        for m in matrix:
            for n in m:
                minimumAbsoluteValue = min(minimumAbsoluteValue, abs(n))
                if n < 0:
                    negativeCount += 1
                    res -= n
                    continue
                res += n

        return (res-(2*minimumAbsoluteValue)) if negativeCount % 2 == 1 else res
