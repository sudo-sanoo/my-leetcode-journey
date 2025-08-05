# To find the longest common prefix, you have to loop through the list of strings and every word in the list.
# But the more intuitive way to solve this is to compare every string using the FIRST string as the base

class Solution(object):
    def longestCommonPrefix(self, strs):
        result = "" #create an empty string to store the prefix 

        #outer loop will iterate the next index when inner loop has finished iterating ALL elements
        #using the first word as the base to compare with every string in the list
        for i in range(len(strs[0])):
            for string in strs: #inner loop iterates every word in the list
                #i == len(string) checks if the current string(word) is too short to have a character at index i, to avoid index error
                #string[i] != strs[0][i] checks/compare if the character at index i in the string(word) matches with the character at index i in the first string(word) in the list
                #if everything matches, the if statement is false and result is updated
                #the inner loop keeps checking until there is a character mismatch and returns the result early
                if i == len(string) or string[i] != strs[0][i]:
                    return result
            result += strs[0][i]

        #return the full common prefix after all checks, only works when ALL the strings(words) in the list are the same
        return result
