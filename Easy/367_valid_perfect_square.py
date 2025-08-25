class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        # Binary Search Approach O(log n)
        if num == 1:
            return True

        a, b = 1, num

        while a <= b:
            mid = (a+b) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                b = mid - 1
            else:
                a = mid + 1

        return False

        '''
        # Math Approach O(sqrt(n))
        x = 1
        while x*x < num:
            x += 1
        
        return x*x == num
        '''

        '''
        # Brute-force approach O(n)
        if num == 1:
            return True

        valid_sq = [x**2 for x in range(1, (num//2)+1)]

        return num in valid_sq
        '''
