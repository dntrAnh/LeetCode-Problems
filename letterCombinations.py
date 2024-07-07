class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        KEYPAD = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl',
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }
        
        if not digits: 
            return []
        
        def backtrack(start): 
            if start == len(digits): 
                result.append(''.join(path))
                return 
            next_num = digits[start]
            for letter in KEYPAD[next_num]: 
                path.append(letter)
                backtrack(start + 1)
                path.pop()
        result = []
        path = []
        backtrack(0)
        return result 
