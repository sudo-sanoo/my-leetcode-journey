import string
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = defaultdict() # first occ of ch
        right = defaultdict() # last occ of ch
        cnt = 0
        for ch in string.ascii_lowercase:
            left[ch] = s.find(ch)
            right[ch] = s.rfind(ch)

            occ = set()
            if left[ch] != -1 and right[ch] - left[ch] >= 2:
                middle = s[left[ch] + 1 : right[ch]]
                for _ in middle:
                    occ.add(_)
                cnt += len(occ)

        return cnt
