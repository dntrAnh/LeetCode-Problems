class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_rolls = sum(rolls) 
        remaining = mean * (n + len(rolls)) - sum_rolls

        if remaining > 6 * n or remaining < n: 
            return []

        distributed_mean = remaining // n 
        mod = remaining % n 
        result = [distributed_mean] * n 
        for idx in range(mod): 
            result[idx] += 1
            
        return result 
