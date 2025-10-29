class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_res=0
        l=0
        seen=set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1

            seen.add(s[r])
            max_res=max(max_res, r-l+1)

        return max_res
