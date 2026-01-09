class Solution:
    def isValid(self, s: str) -> bool:
        # Scenarios:
        #   1. if there is an opening, there should be a closing
        #   2. if there is a closing, and no opening, its invalid
        #   3. if s is a valid parentheses, s will have an even length

        n = len(s)
        if n % 2 != 0:
            return False

        bracketsMap = {"(": ")", "{": "}", "[": "]"}
        closeFirst = []
        
        for pa in s:
            if pa in bracketsMap:
                closeFirst.append(bracketsMap[pa])
            else:
                if not closeFirst or closeFirst.pop() != pa:
                    return False

        return not closeFirst
