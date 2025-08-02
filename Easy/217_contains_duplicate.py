class Solution(object):
    def containsDuplicate(self, nums):
        #runtime complexity of O(n)
        #using sets here is extremely efficient, since a set does not store duplicates
        #creates an empty set
        setNum = set()

        #this for loop will check for duplicate
        for item in nums:
            if item in setNum: #this will check if the same item is added again into the set
                return True #if it is, returns true, and exit the function (return)

            setNum.add(item) #add number/item that has been iterated

        return False #always return False, unless there is a duplicate

        '''
        #starts with item at index 0 
        for item in range(len(nums)):

            #in range of 1 to len(nums) - 1, so index does not go out of bounds
            for check in range(item + 1, len(nums)): 

                if nums[item] == nums[check]:
                    return True
        
        #always return False, unless any value appears twice
        return False

        # This is a bruteforce code that checks an item in the list with every subsequent item
        # in the list for every item in the list, not efficient for large data sets, runtime
        # complexity of O(n**2)

        # The code above passed 65/77 testcases, there are more efficient code
        '''
