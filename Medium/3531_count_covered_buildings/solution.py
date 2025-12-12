class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        max_y = [0] * (n+1)
        min_y = [n+1] * (n+1)
        max_x = [0] * (n+1)
        min_x = [n+1] * (n+1)

        for x, y in buildings:
            max_y[y] = max(max_y[y], x)
            min_y[y] = min(min_y[y], x)
            max_x[x] = max(max_x[x], y)
            min_x[x] = min(min_x[x], y)

        cnt = 0
        for x, y in buildings:
            if (x > min_y[y] and x < max_y[y] and y > min_x[x] and y < max_x[x]):
                cnt += 1

        return cnt
