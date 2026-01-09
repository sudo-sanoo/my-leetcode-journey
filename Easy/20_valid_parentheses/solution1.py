class Solution:
    def isValid(self, s: str) -> bool:
        # Scenarios:
        #   1. if there is an opening, there should be a closing
        #   2. if there is a closing, and no opening, its invalid
        #   3. if s is a valid parentheses, s will have an even length

        n = len(s)
        if n % 2 == 1:
            return False

        closeFirst = []
        
        for pa in s:
            if pa in ")}]" and not closeFirst:
                return False

            if pa == "(":
                closeFirst.append(")")
            elif pa == "{":
                closeFirst.append("}")
            elif pa == "[":
                closeFirst.append("]")
            
            elif pa == ")":
                if closeFirst.pop() != pa:
                    return False
            elif pa == "}":
                if closeFirst.pop() != pa:
                    return False
            elif pa == "]":
                if closeFirst.pop() != pa:
                    return False

        return not closeFirst
