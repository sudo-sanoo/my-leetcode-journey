# What are the conditions of an anagram? The conditions are two words must have the same length, each letter in the word is used exactly once.
# But what that tells us is that if words are sorted a..z, and the result are equal, they are also anagrams
# We can sort words and group the same sorted words together, effectively grouping anagrams

# Question: Why use tuple as the key for Hash Map?
# Answer: Dictionary requires keys to be IMMUTABLE and HASHABLE, and tuple is the perfect data structure for that since it is IMMUTABLE and HASHABLE unlike list, set and dict. 
# Lists, sets, and dicts are mutable (can change), so Python doesn't allow them as keys since their hash could change.

# Question: Why does tuple(sorted(i)) works?
# Answer: sorted(i), when iterating through a for loop returns a list of characters, but lists are not hashable and not immutable, so Python does not allow them as dictionary keys. But tuple freezes the list into a IMMUTABLE and HASHABLE object, so we can use tuple as a key to group matching words

# Bonus: Using an empty string also works since strings are also IMMUTABLE and HASHABLE.
# key = "".join(sorted(i)) also works

# Time complexity of this solution is O(m*n) where
# m is the number of elements(string) in the input list, 
# n is the average length of each string(word),

# Memory complexity of this solution is also O(m*n)
# In the worst case, every word is a different anagram, so the hashmap stores m keys and m lists of words
# Each key is a tuple of length n, so total auxiliary space is proportional to all characters

class Solution(object):
    def groupAnagrams(self, strs):
        hashMap = {}

        for i in strs: #iterate each word in the list
            key = tuple(sorted(i)) #initialize the key as the sorted word for each word
            if key in hashMap:
                hashMap[key].append(i) #append the word as value to the same sorted word that already exists in the hashmap
            else:
                hashMap[key] = [i] #append a new word as the value

        return list(hashMap.values()) #since the values in the hashmap is already a list of anagrams (grouped), simply return the hashmap in the form of a list


