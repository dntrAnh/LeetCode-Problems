class Solution:
    def minSteps(self, n: int) -> int:
        # base case
        if n == 1: 
            return 0 
        
        steps = 0 
        factor = 2
        
        while n > 1: 
            while n % factor == 0: # divisible by 2 
                steps += factor # copy + paste 
                n //= factor
            factor += 1
        
        return steps 
