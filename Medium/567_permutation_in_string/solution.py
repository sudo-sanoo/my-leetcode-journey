class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = defaultdict(int)
        for ch in s1:
            s1map[ch] = s1map.get(ch, 0) + 1

        # somewhere in the iteration of s2, shrink window from l while ch count > in s1map
        # if a ch in s2 is not in s1map, clear all s2map
        # if s2map == s1map in terms of its key and values, return True
        s2map = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            if s2[r] in s1map:
                s2map[s2[r]] = s2map.get(s2[r], 0) + 1
                while s2map[s2[r]] > s1map[s2[r]]:
                    s2map[s2[l]] -= 1
                    l += 1
            else:
                s2map.clear()
                l = r + 1

            if s2map == s1map: return True
        
        return False
