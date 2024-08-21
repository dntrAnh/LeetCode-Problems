class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: 
            return ""
        
        t_count = Counter(t)
        required = len(t_count)

        left, right = 0, 0 
        formed = 0 
        window_counts = defaultdict(int)

        min_len = float('inf')
        min_window = (left, right)

        for right in range(len(s)):
            char = s[right]
            window_counts[char] += 1

            if char in t_count and window_counts[char] == t_count[char]: 
                formed += 1
            
            while left <= right and formed == required: 
                char = s[left]
                if right - left + 1 < min_len: 
                    min_len = right - left + 1 
                    min_window = (left, right) 

                window_counts[char] -= 1 
                if char in t_count and window_counts[char] < t_count[char]: 
                    formed -= 1
                
                left += 1
        
        return "" if min_len == float('inf') else s[min_window[0]:min_window[1] + 1]
