class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        text = text.split(" ")
        c = len(text)

        for word in text:
            for ch in word:
                if ch in brokenLetters:
                    c -= 1
                    break
        
        return c
