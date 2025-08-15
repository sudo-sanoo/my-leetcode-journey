class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # Use a set to store numbers already seen
        # This helps detect loops (if a number repeats, it's not a happy number)
        nSet = set()

        while True:
            result = 0
            #Store the sum of the squares of each digit of n
            for i in str(n):
                i = int(i)
                result += i ** 2
            
            #Check if number is looped again, if it is, return False
            if result in nSet:
                return False
            #Check if result is 1, if it is, return True
            elif result == 1:
                return True
            else:
                #Add the result if not in set and result not equals to 1
                nSet.add(result)

            #Update n as result after adding it to the set for the next while loop iteration
            n = result
