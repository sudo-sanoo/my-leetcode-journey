class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def getMaxUniqueLetters(s):
            maxUnique = 0
            seen = set()
            for ch in s:
                if ch not in seen:
                    maxUnique += 1
                seen.add(ch)
            return maxUnique

        maxUnique = getMaxUniqueLetters(s)
        res = 0
        for currentUnique in range(1, maxUnique + 1):
            l, r, idx, unique, countAtLeastK = 0, 0, 0, 0, 0
            count = {}

            while r < len(s):
                # Expand sliding window
                if unique <= currentUnique:
                    ch = s[r]
                    count[ch] = count.get(ch, 0) + 1
                    if count[ch] == 1:
                        unique += 1
                    if count[ch] == k:
                        countAtLeastK += 1
                    r += 1
                # Shrink sliding window
                else:
                    ch = s[l]
                    if count[ch] == k:
                        countAtLeastK -= 1
                    count[ch] -= 1
                    if count[ch] == 0:
                        unique -= 1
                    l += 1
                
                if (unique == currentUnique and unique == countAtLeastK):
                    res = max(r - l, res)

        return res
