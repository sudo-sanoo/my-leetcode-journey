class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        limit = target[-1]
        for i in range(1, limit+1):
            s.append("Push")

            if i not in target:
                s.append("Pop")

        return s 
