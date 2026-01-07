class Solution:
    def maxArea(self, height: List[int]) -> int:
        # height[l] and height[r] represents the height of the container
        # the water can fill up to the minimum of either height[l] and height[r]
        # the amount of water is obtained via (r-l)*(min(height[r], height[l]), where
        #   the r and l is the width of the container
        #   height[l] and height[r] is the height of the container
        def calc_area(l, r):
            return min(height[l], height[r])*(r-l)

        l, r = 0, len(height)-1
        max_area = float('-inf')
        max_height = max(height)

        while l < r:
            if max_area > (r-l)*(max_height):
                break

            max_area = max(max_area, calc_area(l, r))
            if height[r] >= height[l]:
                l += 1
            else:
                r -= 1

        return max_area
