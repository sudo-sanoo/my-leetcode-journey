class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        drank = numBottles

        while numBottles >= numExchange:
            full = 0

            while numBottles >= numExchange:
                full += 1
                numBottles -= numExchange
                numExchange += 1

            numBottles += full
            
            drank += full

        return drank
