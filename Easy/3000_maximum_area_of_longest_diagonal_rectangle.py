# note: sqrt() function here is not needed, as the greatest diagonal length can be determined without it 
from math import sqrt

class Solution(object):
    def calcLongestDiagonalRectangle(self, rect):
        diagLen = sqrt(rect[0]**2 + rect[1]**2)
        return diagLen

    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        # max() function format: max(iterable, *, key=None, default=None)
        # 1. "dimensions" is passed in as an iterable
        # 2. lambda rect: (self.calcLongestDiagonalRectangle(rect), rect[0] * rect[1]) returns tuple (diagonal length, area)
        # 3. The area is included as a tie-breaker if there are multiple rect with the same diagonal length
        #   - Tuples are compared lexicographically, if they have the same diagonal length, its gonna look at the area
        #   - Lexicographical comparison example: "abcde" and "abcdf", "abcde" will be ranked first, following the alphabetical order
        # 3. The parameter "key=" must pass a function, and the function is applied to every iterable
        # 4. "key=lambda rect:" selects rect (diagonal length, area) as the comparison for max()
        # 5. max() returns the rect (list from "dimensions") with the longest diagonal length, if diagonal tie, pick the one with the largest area
        maxRect = max(dimensions,
                        key=lambda rect: (self.calcLongestDiagonalRectangle(rect), rect[0] * rect[1])
                        )
        
        return maxRect[0] * maxRect[1]
