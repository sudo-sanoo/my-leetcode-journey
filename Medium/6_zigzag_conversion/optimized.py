# numRows = 3, diagonal have 1 char
# numRows = 4, diagonal have 2 char
# numRows = 5, diagonal have 3 char

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>len(s):
            return s

        rows = ['']*numRows
        i = 0
        j = 1
        for char in s:
            rows[i] += char
            if i == 0:
                j=1
            elif i == numRows-1:
                j=-1
            i += j

        return "".join(rows)
