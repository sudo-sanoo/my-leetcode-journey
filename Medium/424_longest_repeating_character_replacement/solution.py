class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Intuition: use sliding window to gauge k.
        #            But, there are 26 alphabeticals,
        #            running 26 for loops then return the max
        #            would probably not pass time constraints.
        #            So, we could use a hashmap to store the number 
        #            of ABCs IN the sliding window.

        abc = defaultdict(int)
        max_freq = 0

        res = 0
        left = 0
        for right in range(len(s)):
            abc[s[right]] = abc.get(s[right], 0) + 1
            max_freq = max(abc[s[right]], max_freq)

            while ((right - left + 1) - max_freq) > k:
                abc[s[left]] -= 1
                left += 1
            
            res = max((right - left + 1), res)

        return res
