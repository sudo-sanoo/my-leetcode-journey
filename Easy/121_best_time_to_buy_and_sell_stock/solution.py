class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if min_price > price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit

        # profit = 0
        # l = 0
        # r = l+1
        # for r in range(1,len(prices)):
        #     while prices[r] < prices[l]:
        #         l += 1

        #     profit = max(prices[r] - prices[l], profit)

        # return 0 if profit <= 0 else profit
