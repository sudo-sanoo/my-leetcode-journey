class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # move vertically 1 unit
        # move horizontally 1 unit
        # move diagonally sqrt(2)
        # moving in any direction is 1 second
        # must visit points in the same order in the array

        seconds = 0
        for i in range(1, len(points)):
            xDiff = points[i][0] - points[i-1][0]
            yDiff = points[i][1] - points[i-1][1]

            seconds += max(abs(xDiff), abs(yDiff))

        return seconds
