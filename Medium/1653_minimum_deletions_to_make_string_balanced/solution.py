class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        left_b = 0
        for ch in s:
            if ch == 'b':
                left_b += 1
            elif left_b:
                res += 1
                left_b -= 1

        return res 
