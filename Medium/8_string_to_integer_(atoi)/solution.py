class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.search(r'^\s*([-+]?\d+)', s)
        if not match: return 0

        num_str = match.group(1)
        num = int(num_str)

        INT_MIN, INT_MAX = -2**31, 2**31-1

        return max(INT_MIN, min(num, INT_MAX))
