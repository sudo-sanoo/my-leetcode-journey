class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Operation 1: Can flip the rightmost bit anytime
        # Operation 2: Flip bits at position i, where i > 0, ONLY IF:
        #               a) The bits at position (i-1) is 1, AND
        #               b) All bits below i-1 (i-2...) must be 0
        def binary_to_gray(n):
            return n ^ (n >> 1)

        def gray_to_binary(gray):
            num = gray
            while gray > 0:
                gray >>= 1
                num ^= gray
            return num

        # Therefore:
        res = n
        while n:
            n >>= 1
            res ^= n
        return res
