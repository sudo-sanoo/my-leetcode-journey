# Using Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        s = [c.lower() for c in s if c.isalnum()]
        l = 0
        r = len(s)-1

        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False

        return True
        
# Using Regex solution
import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower().strip()
        s = re.sub(r"[^a-zA-Z0-9]", " ", s)
        parts = s.split()
        s = "".join(parts)

        return s == s[::-1]
