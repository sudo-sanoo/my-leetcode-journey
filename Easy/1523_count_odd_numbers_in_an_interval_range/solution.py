class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = (high-low)//2
        return n if (low % 2 == 0 and high % 2 == 0) else n+1
