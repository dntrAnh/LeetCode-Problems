class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return len(set(s)) < len(s)
        
        diffs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append((s[i], goal[i]))
        
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
