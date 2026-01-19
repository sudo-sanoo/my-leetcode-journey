class Solution:
    def fib(self, n: int) -> int:
        # bruteforce recursion (not very optimized)
        # if n = 4
        # F(4) = F(3) + F(2)
        #      = [ F(2) + F(1) ] + [ F(1) + F(0) ]
        #      = { [ F(1) + F(0) ] + F(1) } + [ F(1) + F(0) ]

        if n <= 1:
            return n if n >= 0 else 0

        return self.fib(n-1) + self.fib(n-2)
