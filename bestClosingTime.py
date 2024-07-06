class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix, suffix = [0] * (n + 1), [0] * (n + 1)
        result = [0] * (n + 1)
        
        for i in range(1, n + 1): 
            if customers[i - 1] == 'N': 
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]
        
        for i in range(n - 1, -1, -1): 
            if customers[i] == 'Y': 
                suffix[i] = suffix[i + 1] + 1
            else:
                suffix[i] = suffix[i + 1]
        
        for i in range(n + 1): 
            result[i] = prefix[i] + suffix[i]

        min_val = min(result)
        return result.index(min_val)
