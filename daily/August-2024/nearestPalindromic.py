class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num_length = len(n)
        if n == "1":
            return "0"
        
        prefix_value = int(n[:(num_length + 1) // 2])
        palindrome_candidates = {str(10**(num_length-1) - 1), str(10**num_length + 1)}
        
        for adjustment in [-1, 0, 1]:
            new_prefix = str(prefix_value + adjustment)
            if num_length % 2 == 0:
                palindrome_candidates.add(new_prefix + new_prefix[::-1])
            else:
                palindrome_candidates.add(new_prefix + new_prefix[:-1][::-1])
        
        palindrome_candidates.discard(n)
        
        return min(palindrome_candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
