class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ch_bij = {}
        word_bij = {}
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        for ch, word in zip(pattern, words):
            if ch in ch_bij and ch_bij[ch] != word:
                return False
            if word in word_bij and word_bij[word] != ch:
                return False
            
            ch_bij[ch] = word
            word_bij[word] = ch

        return True
            
