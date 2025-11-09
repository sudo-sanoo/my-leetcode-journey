from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        # Counter() makes a mapping of key to its value (calculated automatically)
        need = Counter(word2)
        have = Counter()
        res = 0
        l = 0
        required = len(need)
        formed = 0

        for r, ch in enumerate(word1):
            have[ch] += 1
            
            if ch in need and have[ch] == need[ch]:
                formed += 1

            # Shrink window while it's valid
            while formed == required:
                # every substring starting from l to r (inclusive)
                # and any earlier start (<= l) will also be valid
                res += len(word1)-r

                # move left pointer to look for smaller valid window
                leftChar = word1[l]
                have[leftChar] -= 1
                if leftChar in need and have[leftChar] < need[leftChar]:
                    formed -= 1
                l += 1
                
        return res
