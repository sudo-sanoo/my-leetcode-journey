# Note: "Hash Table" does not mean we need to use a hashmap, it basically means to use any data structure with O(1) average lookups
# The key here is to know what are the numbers in the input is the start of a sequence, and if the number - 1 is not in the list means that it is the start of a sequence.
# First, you can iterate through one sequence and it is the largest sequence (if there are no other sequence, that is the largest sequence)
# But there are multiple sequences in a list, so how do you know and return the largest sequence from the input list?
# Second, you can iterate the next sequence and compare with the previous sequence and keep whichever sequence is the largest
# This way, wherever the largest sequence is started from (num - 1 not in input list), will be compared with other sequences and return the largest sequence after iterating every (num - 1 not in input list)

class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums) #using sets to omit duplicates
        max_length = 0 #initialize current max_length, in the case of a no sequence input

        for num in numSet:
            if num - 1 in numSet: #if num - 1 is in the list, it is not the start of a sequence
                continue #therefore, continue to the next num in the input
            else:
                start = num #initialize the start of the sequnce
                current_length = 1  #start counting the length of the sequence 

                while start + 1 in numSet: #the count will keep incrementing until the end of a num+1 sequence
                    start += 1
                    current_length += 1

                max_length = max(max_length, current_length) #then compare the current sequence with the previous sequence 

        return max_length
                
