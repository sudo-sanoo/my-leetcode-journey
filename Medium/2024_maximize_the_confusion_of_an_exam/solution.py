class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        if n == 1:
            return 1

        cnt_F = 0
        max_T = 0
        l = 0
        for r in range(n):
            if answerKey[r] == 'F':
                cnt_F += 1
            while cnt_F > k:
                if answerKey[l] == 'F':
                    cnt_F -= 1
                l += 1
            max_T = max(r-l+1, max_T)

        cnt_T = 0
        max_F = 0
        l = 0
        for r in range(n):
            if answerKey[r] == 'T':
                cnt_T += 1
            while cnt_T > k:
                if answerKey[l] == "T":
                    cnt_T -= 1
                l += 1
            max_F = max(r-l+1, max_F)

        return max(max_T, max_F)
