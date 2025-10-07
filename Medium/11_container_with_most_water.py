class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # index represents the length (x-axis)
        # value represents the height (y-axis)

        l = 0
        r = len(height)-1
        max_area = 0

        while l < r:
            xd = r - l
            yd = min(height[l], height[r])

            cur_area = xd * yd
            max_area = max(cur_area, max_area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_area
