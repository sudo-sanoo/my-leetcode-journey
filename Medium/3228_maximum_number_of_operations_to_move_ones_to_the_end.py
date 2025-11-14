class Solution:
    def maxOperations(self, s: str) -> int:
        one_passed = 0 #no. of 1's passed before encoutering a 0
        res = 0
        i = 0
        while i < len(s):
            if s[i] == "0":
                while (i+1 < len(s)) and (s[i+1] == "0"):
                    i += 1
                res += one_passed
            else:
                one_passed += 1
            i += 1

        return res
                
