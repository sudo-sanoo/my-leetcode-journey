class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        n -= 1
        op = 1
        while n >= 1:
            if op > 4:
                op = 1

            if op == 1:
                x = stack.pop() * n
                stack.append(x)
            elif op == 2:
                x = stack.pop() // n
                stack.append(x)
            elif op == 3:
                stack.append("+")
                stack.append(n)
            elif op == 4:
                stack.append("-")
                stack.append(n)
            
            op += 1
            n -= 1

        res = stack[0]
        for i in range(len(stack)):
            if stack[i] == "+":
                res += stack[i+1]
            elif stack[i] == "-":
                res -= stack[i+1]
            else:
                continue

        return res
