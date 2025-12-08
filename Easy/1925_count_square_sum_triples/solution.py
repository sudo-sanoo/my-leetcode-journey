class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n):
            for b in range(a, n):
                x = math.sqrt(a**2 + b**2)
                if x > n:
                    break
                if (x*10)%10 == 0:
                    cnt += 2

        return cnt
