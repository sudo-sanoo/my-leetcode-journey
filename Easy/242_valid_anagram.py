class Solution(object):
    def isAnagram(self, s, t):
        #Approach 1: Using HashMap to count the occurence of each letters.
        #The idea of approach 1 is to check if the occurence of each letter exists in the other
        #Store each letter as a key and the number of occurence as a value
        #If the other string matches the exact letters and the number of their occurences,
        #then it is an anagram
        #Time complexity of O(s + t), because we are iterating two strings
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

        '''
        #Approach 2: Using Counter()
        #Counter() is a data structure in Python, that automatically counts things
        #Passing both string to the Counter() and if they're exactly equal, return True
        #Runtime Complexity of O(s + t)
        return Counter(s) == Counter(t)
        '''

        '''
        #Approach 3: Using Sorted()
        #The first and second approach utilizes O(s + t) memory
        #So, is there a way to use O(1) memory?
        #Yes, using sort to sort the order of strings then compare. If they are equal, returns
        # True
        #However, the built-in sorting algorithms usually uses O(nlogn) time
        return sorted(s) == sorted(t)
        '''
