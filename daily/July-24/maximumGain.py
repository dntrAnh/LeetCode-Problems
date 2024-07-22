class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substr(str, letter_1, letter_2, point): 
            stack = []
            points = 0
            for char in s: 
                if stack and stack[-1] == letter_1 and char == letter_2: 
                    stack.pop() 
                    points += point 
                else: 
                    stack.append(char)
            return ''.join(stack), points
            
        if x > y: # remove "ab" first 
            s, score_1 = remove_substr(s, 'a', 'b', x)
            s, score_2 = remove_substr(s, 'b', 'a', y) 
        else: # remove "ba" first
            s, score_1 = remove_substr(s, 'b', 'a', y)
            s, score_2 = remove_substr(s, 'a', 'b', x) 
        
        return score_1 + score_2 
