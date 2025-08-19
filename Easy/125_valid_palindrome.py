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
