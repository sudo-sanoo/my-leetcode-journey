# numRows = 3, diagonal have 1 char
# numRows = 4, diagonal have 2 char
# numRows = 5, diagonal have 3 char

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n: return s
        numCols = (n//numRows) + (n//numRows) * (numRows-2) + 1

        matrix = [[""] * numCols for _ in range(numRows)]

        # build verticals and diagonals
        i = 0
        j = 0
        idx = 0
        going_down = True
        while idx < n:
            matrix[i][j] = s[idx]

            if i == numRows-1:
                going_down = False
            elif i == 0:
                going_down = True

            if going_down:
                i += 1
            else:
                i -= 1
                j += 1
            
            idx+=1

        res = ""
        for r in range(numRows):
            for c in range(numCols):
                if matrix[r][c]: res+=matrix[r][c]

        return res
