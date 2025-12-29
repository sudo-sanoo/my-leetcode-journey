class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for m in grid:
            l = 0
            r = len(m)-1
            while l<r:
                mid = l + (r-l) // 2
                if m[mid] < 0:
                    r = mid
                else:
                    l = mid+1

            if m[r] >= 0:
                continue

            cnt += len(m)-r

        return cnt
