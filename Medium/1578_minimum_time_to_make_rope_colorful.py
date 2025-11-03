class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        # More optimized solution (Two Pointers)
        res, l = 0, 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] > neededTime[r]:
                    res += neededTime[r]
                else:
                    res += neededTime[l]
                    l = r
            else:
                l = r
        return res

        # Optimized Solution
        res = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                res += min(neededTime[i], neededTime[i-1])
                # Keep the larger neededTime (cuz we already used the minimum, added to res)
                # Update the current neededTime for the next min() comparison
                neededTime[i] = max(neededTime[i], neededTime[i-1])
        return res

        # Initial Solution (Idea)
        res = 0
        prevColor = colors[0]
        prevTime = neededTime[0]
        time = []
        for i, c, t in zip(range(len(colors)), colors, neededTime):
            if c == prevColor:
                if i == 0:
                    continue
                if not time:
                    time.append(prevTime)
                time.append(t)
            else:
                if time:
                    res += (sum(time) - max(time))
                    time = []

            prevColor = c
            prevTime = t

        if time:
            res += (sum(time) - max(time))

        return res
