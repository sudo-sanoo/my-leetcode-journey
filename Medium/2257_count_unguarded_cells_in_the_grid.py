class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        # Create the grid
        # 0 - free, 1 - wall, 2 - guard, 3 - guarded
        grid = [[0] * n for _ in range(m)]

        # Mark the grid cells accordingly
        for r, c in guards:
            grid[r][c] = 2
        for r, c in walls:
            grid[r][c] = 1

        # Helper function to mark the guarded areas
        def mark_guarded(r, c):
            # Move down
            for row in xrange(r+1, m):
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3
            # Move up
            for row in reversed(xrange(0, r)):
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3
            # Move right
            for col in xrange(c+1, n):
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3
            # Move left
            for col in reversed(xrange(0, c)):
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3

        for r, c in guards:
            mark_guarded(r, c)

        total = 0
        for row in grid:
            for col in row:
                if col == 0:
                    total += 1

        return total
