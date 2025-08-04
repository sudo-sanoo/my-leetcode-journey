#The idea of an anagram is to check if the occurence of each letter exists in the other
#Store each letter as a key and the number of occurence as a value
#If the other string matches the exact letters and the number of their occurences, then it is an anagram

class Solution(object):
    def isAnagram(self, s, t):
        freqS = {}
        freqT = {}

        for character in s:
            if character in freqS:
                freqS[character] += 1
            else:
                freqS[character] = 1

        for character in t:
            if character in freqT:
                freqT[character] += 1
            else:
                freqT[character] = 1

        if freqS == freqT:
            return True

        return False
