class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        consecutive_zeroes = 0
        for ch in s:
            if ch == "1":
                consecutive_zeroes += 1
                res += consecutive_zeroes
            else:
                consecutive_zeroes = 0

        return (res % ((10**9)+7))
