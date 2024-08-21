class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        if n < 5:
            return 0
        
        left = 0
        result = 0
        count = 1
        
        for right in range(1, n):
            if word[right] >= word[right - 1]:
                if word[right] > word[right - 1]:
                    count += 1
            else:
                count = 1
                left = right
            
            if count == 5:
                result = max(result, right - left + 1)
        
        return result
