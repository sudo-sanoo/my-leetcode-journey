class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        start = 0
        end = len(needle) - 1

        for s in range(len(haystack)-len(needle)+1):
            if needle[start] == haystack[s] and needle[end] == haystack[s+end]:
                if needle[start:end] == haystack[s:s+end]:
                    return s

        return -1
