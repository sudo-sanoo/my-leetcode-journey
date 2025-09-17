class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote, magazine = list(ransomNote), list(magazine)
        r = {}
        m = {}

        for i in ransomNote:
            if i not in r:
                r[i] = 1
            else:
                r[i] += 1

        for j in magazine:
            if j not in m:
                m[j] = 1
            else:
                m[j] += 1

        for ch, count in r.items():
            if ch not in m or m[ch] < count:
                return False

        return True
