class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<=r:
            if s[l] != s[r]:
                return False
            l+=1; r-=1
        return True

    def backtracking(self, s: str, res: List[List[str]], temp: List[str]) -> None:
        if len(s) == 0:
            res.append(temp[:])
            return
        for i in range(len(s)):
            part = s[0:i+1]
            if self.isPalindrome(part):
                temp.append(part)
                self.backtracking(s[i+1:], res, temp)
                temp.pop()

    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        self.backtracking(s, res, temp)

        return res
