class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        if row < 3 or col < 3:
            return 0

        # a 3x3 magic square has distinct numbers ranging from 1-9, have a sum of 45
        # meaning each row, column and diagonal of a 3x3 should each have a sum of EXACTLY 15
        # valid numbers are 0 < grid[row][col] < 10, where grid[row][col] are the valid numbers 
        # there can be up to 10 rows and 10 columns

        def isMagicSquare(r, c):
            items = []
            for i in range(3):
                for j in range(3):
                    items.append(grid[r+i][c+j])

            if sorted(items) != [1,2,3,4,5,6,7,8,9]:
                return False

            # Check rows sum
            if sum(grid[r][c:c+3]) != 15: return False
            if sum(grid[r+1][c:c+3]) != 15: return False
            if sum(grid[r+2][c:c+3]) != 15: return False
            
            # Check columns sum
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15: return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15: return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15: return False
            
            # Check diagonals sum
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15: return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15: return False
            
            return True

        res = 0
        for r in range(row-3+1):
            for c in range(col-3+1):
                if isMagicSquare(r, c):
                    res += 1

        return res
