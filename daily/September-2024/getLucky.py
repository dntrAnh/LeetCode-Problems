class Solution:
    def getLucky(self, s: str, k: int) -> int:
        stack = []
        for ch in s: 
            stack.append(str(ord(ch) - ord('a') + 1))
        
        result = ''.join(stack) 
        while k: 
            curr_sum = 0
            for ch in result: 
                curr_sum += int(ch) 
                print(curr_sum) 
            result = str(curr_sum)
            k -= 1

        return int(result) 
