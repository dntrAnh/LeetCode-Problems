class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_counts = [0] * 26
        for ch in word: 
            letter_counts[ord(ch) - ord('a')] += 1

        sorted_counts = sorted(letter_counts, reverse=True) 

        total_presses = 0 
        for idx, count in enumerate(sorted_counts): 
            if count == 0: 
                break 
            total_presses += (idx // 8 + 1) * count 

        return total_presses
