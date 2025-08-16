class Solution(object):
    def maximum69Number (self, num, method="math"):
        """
        :type num: int
        :rtype: int
        """
        if method == "math":
            return self.mathApproach(num)
        else:
            return self.stringApproach(num)
        
    # Math Approach
    def mathApproach(self, num):
        x = len(str(num)) - 1 #exponential value

        for i in str(num):
            i = int(i)

            #Only need to find if we need to flip the FIRST 6 to 9
            if i != 6:
                #If the current iteration is not 6, the exponential decreases
                x -= 1
                #skip the rest to the next iteration
                continue
            else:
                #To flip 6 to 9, just add 3
                #Determine the value by using an exponent of 10
                return num + 3*10**x

        return num

    #String Approach
    #Replace the first occurence of a 6, if no 6 return default value
    def stringApproach(self, num):
        return int(str(num).replace("6", "9", 1))
