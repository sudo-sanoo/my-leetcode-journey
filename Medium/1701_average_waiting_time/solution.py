class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        clock = customers[0][0]
        waiting_time = 0
        for arrival, time in customers:
            if arrival > clock:
                clock = arrival
            clock += time
            waiting_time += clock - arrival

        return waiting_time / len(customers)

        # Solution above is faster
        # clock = customers[0][0]
        # waiting_time = 0
        # for c in customers:
        #     if c[0] > clock:
        #         clock = c[0]
        #     clock += c[1]
        #     waiting_time += clock - c[0]

        # return waiting_time / len(customers)
