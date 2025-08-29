class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        sorted_odd_freq = sorted(
            [(ch, count) for ch, count in freq.items() if count % 2 != 0],
            key=lambda item: item[1],
            reverse=True
        )
        sorted_even_freq = sorted(
            [(ch, count) for ch, count in freq.items() if count % 2 == 0],
            key=lambda item: item[1]
        )

        return sorted_odd_freq[0][1] - sorted_even_freq[0][1]
