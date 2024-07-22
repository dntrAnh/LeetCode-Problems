class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        num_customers = len(customers)
        time_waiting = customers[0][1]
        prev_finished = customers[0][0] + customers[0][1]

        for idx in range(1, num_customers): 
            times = customers[idx] 
            arrive = times[0] 

            start = max(arrive, prev_finished) 
            end = start + times[1]
            prev_finished = end
            time_waiting += end - arrive 
        
        return time_waiting / num_customers 
