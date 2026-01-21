class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log (m*n)) = O(log(m) + log(n))
        # meaning perform a binary search over m, then over n, sequentially

        # Lm = Left(m), Rm = Right(m), Mm = Mid(m)
        # Ln = Left(n), Rn = Right(n), Mn = Mid(n)

        Lm = 0
        Rm = len(matrix) - 1
        while Lm < Rm:
            Mm = Lm + (Rm-Lm)//2

            if matrix[Mm][0] == target:
                return True
            elif matrix[Mm][0] > target:
                Rm = Mm - 1
            else:
                Lm = Mm + 1

        if Lm > 0:
            Lm = Lm-1 if matrix[Lm][0] > target else Lm

        Ln = 0
        Rn = len(matrix[0]) - 1
        while Ln <= Rn:
            Mn = Ln + (Rn-Ln)//2

            if matrix[Lm][Mn] == target:
                return True
            elif matrix[Lm][Mn] > target:
                Rn = Mn - 1
            else:
                Ln = Mn + 1

        return False
