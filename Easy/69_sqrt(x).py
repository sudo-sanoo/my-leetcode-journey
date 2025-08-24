class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        low = 1
        high = x // 2
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid  # for perfect square numbers, will eventually return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
                ans = mid # however for non-perfect square numbers, store the floored integers as ans

        return ans # return ans when the loop breaks (will break for non-perfect square numbers)
