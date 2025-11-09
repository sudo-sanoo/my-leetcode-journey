class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        def op1(num1, num2):
            return num1-num2
        def op2(num1, num2):
            return num2-num1
        
        res = 0
        while True:
            if num1 <= 0:
                break
            if num2 <= 0:
                break

            if num1 >= num2:
                num1 = op1(num1, num2)
                res += 1
            else:
                num2 = op2(num1, num2)
                res += 1

        return res
