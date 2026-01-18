class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        # compute prefix sum for rows
        prefix_r = [[0] * C for _ in range(R)]
        for r in range(R):
            prefix_r[r][0] = grid[r][0]
            for c in range(1, C):
                prefix_r[r][c] = (prefix_r[r][c-1] + grid[r][c])

        # compute prefix sum for cols
        prefix_c = [[0] * C for _ in range(R)]
        for c in range(C):
            prefix_c[0][c] = grid[0][c]
            for r in range(1, R):
                prefix_c[r][c] = (prefix_c[r-1][c] + grid[r][c])

        # compute prefix sum for main diagonal and anti diagonal
        prefix_d1 = [[0] * C for _ in range(R)]
        prefix_d2 = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                # compute prefix sum for main diagonal
                prev_d1 = prefix_d1[r-1][c-1] if (r > 0 and c > 0) else 0
                prefix_d1[r][c] = grid[r][c] + prev_d1

                # compute prefix sum for anti diagonal
                prev_d2 = prefix_d2[r-1][c+1] if (r > 0 and c < C - 1) else 0
                prefix_d2[r][c] = grid[r][c] + prev_d2

        # helper functions
        def row_sum(r, c1, c2):
            return prefix_r[r][c2] - (prefix_r[r][c1-1] if c1 > 0 else 0)
        def col_sum(c, r1, r2):
            return prefix_c[r2][c] - (prefix_c[r1-1][c] if r1 > 0 else 0)
        def diag1_sum(r, c, k):
            r2, c2 = r+k-1, c+k-1
            return prefix_d1[r2][c2] - (prefix_d1[r-1][c-1] if r > 0 and c > 0 else 0)
        def diag2_sum(r, c, k):
            r2, c2 = r + k - 1, c - (k - 1)
            return prefix_d2[r2][c2] - (prefix_d2[r-1][c+1] if r > 0 and c+1 < C else 0)

        # magic square check
        for k in range(min(R, C), 0, -1): # 4, 3, 2, 1
            for i in range(R-k+1): # 0, 1
                for j in range(C-k+1): # 0, 1, 2
                    
                    target = row_sum(i, j, j+k-1)
                    cont = True # just a variable to see if can continue or not

                    # check rows
                    for r in range(i, i+k):
                        if row_sum(r, j, j+k-1) != target:
                            cont = False
                            break

                    # check cols
                    if cont:
                        for c in range(j, j+k):
                            if col_sum(c, i, i+k-1) != target:
                                cont = False
                                break

                    # check diagonals
                    if cont:
                        if diag1_sum(i, j, k) != target:
                            cont = False
                        elif diag2_sum(i, j+k-1, k) != target:
                            cont = False

                    # if all checks passes, can return the length of the magic square
                    if cont:
                        return k

        return
