class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Optimized solution
        # Sort by end ascending, start ascending
        intervals.sort(key=lambda item: (item[1], -item[0]))
        a, b = -1, -1 # a and b are the last two chosen points 
        count = 0
        for L, R in intervals:
            inside_a = (L <= a <= R)
            inside_b = (L <= b <= R)

            if inside_a and inside_b:
                continue
            if inside_b:
                count += 1
                a = b
                b = R
            else:
                count += 2
                a = R - 1
                b = R
            
        return count


        # Semi Brute-force solution (Implementation of idea)
        # Step 1: Sort each interval in intervals by the R value (interval = [L,R])
        intervals.sort(key=lambda item: item[1])

        # Step 2: Initialize set with default values
        container = {intervals[0][1], intervals[0][1]-1}

        # Step 3: Keep track of the numbers in container and check if they are within range of the current interval
        for interval in intervals:
            L, R = interval[0], interval[1]

            cnt_in_range = sum(1 for val in container if L <= val <= R)

            if cnt_in_range == 2:
                continue
            elif cnt_in_range == 1:
                if R in container:
                    container.add(R-1)
                else:
                    container.add(R)
            elif cnt_in_range == 0:
                container.add(R)
                container.add(R-1)

        return len(container)
