class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        answer = [0] * len(boxes)
        
        ballsToLeft = movesToLeft = 0
        ballsToRight = movesToRight = 0

        for i in range(len(boxes)):
            answer[i] += movesToLeft
            ballsToLeft += int(boxes[i])
            movesToLeft += ballsToLeft

            j = len(boxes) - 1 - i
            answer[j] += movesToRight
            ballsToRight += int(boxes[j])
            movesToRight += ballsToRight

        return answer
