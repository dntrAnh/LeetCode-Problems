class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating) 
        count = 0 

        for i in range(n): 
            left_less = left_greater = right_less = right_greater = 0
            
            for j in range(i): 
                if rating[j] < rating[i]: 
                    left_less += 1
                else: 
                    left_greater += 1 
            
            for k in range(i + 1, n): 
                if rating[k] < rating[i]: 
                    right_less += 1
                else: 
                    right_greater += 1
            
            count += left_less * right_greater + left_greater * right_less 
        
        return count
