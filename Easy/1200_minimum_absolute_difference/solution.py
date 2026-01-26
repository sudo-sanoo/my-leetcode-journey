class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_diff = float('inf')
        min_map = defaultdict(list)
        arr.sort()
        for i in range(1, len(arr)):
            x = arr[i] - arr[i-1]
            if x <= min_diff:
                min_map[x].append([ arr[i-1], arr[i] ])
                min_diff = x

        return min_map[min_diff]
