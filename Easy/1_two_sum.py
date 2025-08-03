#The idea is that num[x] + num[y] == target, and return the index of both numbers in
#the list 
#If num[x] + num[y] == target, what is the most efficient way or how quickly can I
#find num[y] if I know what num[x] is?
#Is there a more efficient approach for accessing indices? Yes, hashmaps lets us check
#if the complement already exists in constant time.
#What should I store in the hashmap? Store num[x] as the key and its index as value
#While iterating, we check if (target - num[x]) already exists in the hashmap, if it is
#we found the pair, and return their indices 

class Solution(object):
    def twoSum(self, nums, target):

        numMap = {} # creates empty dictionary

        # enumerate() loops throught a list and get both index and value in a list
        # enumerate() returns something like [{0: nums[0]}, {1: nums[1]}, {2: nums[2]}...]
        for index, value in enumerate(nums):
            if target - value not in numMap: # if the number (target - value) is not yet in the numMap,
                numMap[value] = index # map an index to value (key)
            else:
                return [numMap[target-value], index] #returns the index mapped to the value and the current index in the iteration

        return -1

        '''
        #Brute force approach: check every single combination of numbers
        #Runtime Complexity: O(n**2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        '''
