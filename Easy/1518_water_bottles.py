class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # given numBottles as the initial number of filled bottles you can drink (first set)
        # after the first set, you will have equal numBottles of empty bottles, where these can be used to exchanged for filled bottles 
        # the number of empty bottles that can be exchanged for 1 filled bottle is numExchange
        # find the number of filled bottles in total from the first set, to the final set, where in the final set, the number of empty bottles < numExchange

        res = 0
        drank = numBottles

        while numBottles >= numExchange:
            res += drank

            if numBottles % numExchange == 0:
                drank = numBottles // numExchange
                numBottles = drank
            else:
                rem = numBottles % numExchange
                drank = numBottles // numExchange
                numBottles = drank + rem

        return res + drank
