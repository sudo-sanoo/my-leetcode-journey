class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        L, R = 0, n-1
        trapped = 0
        left_max, right_max = 0, 0

        while L < R:
            left_max = max(left_max, height[L])
            right_max = max(right_max, height[R])

            if height[L] >= height[R]:
                wR = (right_max - height[R])
                trapped += wR if wR > 0 else 0
                R -= 1
            else:
                wL = (left_max - height[L])
                trapped += wL if wL > 0 else 0
                L += 1

        return trapped
