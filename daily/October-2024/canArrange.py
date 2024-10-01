class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        num_freq = [0] * k 

        for num in arr: 
            remainder = (num % k + k) % k 
            num_freq[remainder] += 1
        
        if num_freq[0] % 2 != 0: 
            return False 
        
        for i in range(1, k // 2 + 1): 
            if num_freq[i] != num_freq[k - i]:
                return False 
        
        return True 
