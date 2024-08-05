class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr) 
        for ch in arr: 
            if counter[ch] == 1: 
                k -= 1
                if k == 0: 
                    return ch 
        return ''
