class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels_freq = {}
        cons_freq = {}
        vowels = ["a", "e", "i", "o", "u"]

        for ch in s:
            if ch in vowels:
                if ch not in vowels_freq:
                    vowels_freq[ch] = 1
                else:
                    vowels_freq[ch] += 1
            else:
                if ch not in cons_freq:
                    cons_freq[ch] = 1
                else:
                    cons_freq[ch] += 1

        if not vowels_freq:
            vowels_freq_val = 0
        else:
            vowels_freq_val = max(vowels_freq.values())
        
        if not cons_freq:
            cons_freq_val = 0
        else:
            cons_freq_val = max(cons_freq.values())

        return vowels_freq_val + cons_freq_val
