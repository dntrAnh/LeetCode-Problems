class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_cost = sum(cost)
        sum_gas = sum(gas)

        if sum_cost > sum_gas: 
            return -1 
        
        curr_gas = 0 
        start_idx = 0 

        for i in range(len(gas)): 
            curr_gas += gas[i] - cost[i]
            if curr_gas < 0: 
                curr_gas = 0 
                start_idx = i + 1
        
        return start_idx
