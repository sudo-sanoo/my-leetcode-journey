# Time Complexity: O(n)
# Iterating through the input roman numeral is O(n), where n is the number of roman numerals

# Memory Complexity: O(1)
# The values dictionary always has the same 7 Roman numeral mappings, no matter how long the input string is, which means it takes Constant Space: O(1)
# total and i store single integer values
# not creating an array, list, or dictionary whose size depends on the number of characters in s

# Hash the integer value to each of its roman numerals
# Iterate the roman numerals input, if the value of the first roman numeral is less than the value of the second roman numeral, decrease the value of the iterating roman numeral from the result
# For example IV, I(1) is less than V(5), so reducing the value of the first numeral from the total (0 - 1) gives us -1. So, all we have to do is just add the final roman numeral from the input, V (-1 + 5), which makes total = 4 = IV.
# Note: we have to add the final roman numeral explicitly because the for loop if-condition is false, and will exit the loop without iterating the final roman numeral from the input 

class Solution(object):
    def romanToInt(self, s):
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0

        for i in range(len(s) - 1):
            if values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        total += values[s[-1]]

        return total
