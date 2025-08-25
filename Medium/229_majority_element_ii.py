class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        # Using list comprehension
        #   - freq.items() gives a sequence of key, value pairs
        #   - for key, value loops through each key, value pairs from the dictionary
        #   - if value > len(nums)/3 compares the value to the length of the list divided by 3
        #   - [key...] makes a new list containing all the keys that satisfy the condition
        # result = [key for key, value in freq.items() if value > len(nums)/3]

        # Using filter + lambda
        #6. list() stores every key in a list in "result"
        result = list(
            #5. map() extracts only the key from the key, value pairs
            map(
                #4. lambda item: item[0] selects the key from a key, value pairs
                lambda item: item[0], 
                #1. freq.items() gives a sequence of key, value pairs
                #2. lambda item: item[1] selects the value from a key, value pair
                #3. filter(... > len(nums)/3, ...) only keep the key, value pair where the value is greater than len(nums)/3
                filter(lambda item: item[1] > len(nums)/3, freq.items())
            )
        )

        return result
