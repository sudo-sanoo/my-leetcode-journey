class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ret=0
        for string in zip(*strs):
            if string != tuple(sorted(string)):
                ret+=1
        return ret
