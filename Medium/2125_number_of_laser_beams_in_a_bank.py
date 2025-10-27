class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        res=0
        cnt=0
        for row in bank:
            cur_cnt=0
            for col in row:
                if col == "1":
                    cur_cnt+=1
            
            if cur_cnt == 0:
                continue

            beams=(cur_cnt*cnt)
            res+=beams
            cnt=cur_cnt

        return res
