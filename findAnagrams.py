class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashmap = defaultdict(int) 
        p_count = Counter(p) 
        left = 0 
        result = []

        n = len(p)

        for right in range(len(s)): 
            hashmap[s[right]] += 1

            if right - left + 1 > n: 
                if hashmap[s[left]] == 1: 
                    del hashmap[s[left]] 
                else: 
                    hashmap[s[left]] -= 1
                left += 1
            
            if hashmap == p_count: 
                result.append(left) 
        
        return result            
