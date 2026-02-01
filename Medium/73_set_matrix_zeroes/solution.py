class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        vertical = set()
        horizontal = set()
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == 0:
                    vertical.add(n)
                    horizontal.add(m)

        for v in vertical:
            for m in range(len(matrix)):
                matrix[m][v] = 0

        for h in horizontal:
            for n in range(len(matrix[0])):
                matrix[h][n] = 0

        
