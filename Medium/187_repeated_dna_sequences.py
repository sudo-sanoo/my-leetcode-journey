class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=set()
        seen=set()

        for i in range(len(s)-9):
            x = s[i:i+10]

            if x in seen:
                res.add(x)
            else:
                seen.add(x)

        return list(res)
