class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = eating speed per hour
        # Koko has 'h' hour to eat 'k' bananas per hour

        k_min = (sum(piles) + (h-1)) // h # ceiling for sum(piles) / h
        k_max = max(piles)

        if len(piles) == h:
            return k_max

        L, R = k_min, k_max
        while L < R:
            k = L + ((R - L) // 2)
            total_hours_needed_at_speed_k = sum((p + k - 1) // k for p in piles)

            if h >= total_hours_needed_at_speed_k:
                R = k
            else:
                L = k + 1

        return L
