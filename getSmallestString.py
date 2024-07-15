class Solution:
    def getSmallestString(self, s: str) -> str:
        def sameParity(a, b): 
            num_a = int(a)
            num_b = int(b)
            if ((num_a % 2 == 0) and (num_b % 2 == 0)) or ((num_a % 2 != 0) and (num_b % 2 != 0)): 
                return True 
            return False 
        
        s = list(s)
        n = len(s)
        
        for i in range(1, n): 
            if sameParity(s[i - 1], s[i]): 
                if s[i - 1] > s[i]: 
                    s[i - 1], s[i] = s[i], s[i - 1] 
                    break 
        
        return ''.join(s)
