class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == n: 
            return -1 
        
        trust_count = [0] * (n + 1)

        for person_a, person_b in trust: 
            trust_count[person_a] -= 1
            trust_count[person_b] += 1
        
        for i in range(1, n + 1): 
            if trust_count[i] == n - 1: 
                return i 
        
        return -1
