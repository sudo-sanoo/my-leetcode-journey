class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n == 1 and digits[0] == 9:
            return [1,0]
        if n == 1:
            return [digits[0]+1]

        digits[-1] += 1
        for i in range(n-1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1

        return [1]+[0]*(n) if digits[0] == 0 else digits
