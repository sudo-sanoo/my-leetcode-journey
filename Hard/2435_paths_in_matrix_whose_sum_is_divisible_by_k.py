class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cache = [[[-1] * k for _ in range(COLS)] for _ in range(ROWS)]
        MOD = 10**9 + 7
        def dfs(r, c, remain):
            if r == ROWS - 1 and c == COLS - 1:
                remain = (remain + grid[r][c]) % k
                return 0 if remain else 1
            if r == ROWS or c == COLS:
                return 0
            if cache[r][c][remain] > -1:
                return cache[r][c][remain]

            cache[r][c][remain] = (
                dfs(r + 1, c, (remain + grid[r][c]) % k) % MOD +
                dfs(r, c + 1, (remain + grid[r][c]) % k) % MOD
            ) % MOD

            return cache[r][c][remain]

        return dfs(0, 0, 0)
