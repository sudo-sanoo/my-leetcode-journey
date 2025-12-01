class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "C":
                stack.pop()
            elif o == "D":
                x = int(stack[-1]) * 2
                stack.append(x)
            elif o == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(o))

        return sum(stack)
