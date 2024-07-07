class Solution:
    def validStrings(self, n: int) -> List[str]:
        def is_valid_binary_string(binary_str):
            for i in range(len(binary_str) - 1):
                if binary_str[i] == '0' and binary_str[i + 1] == '0':
                    return False
            return True
        
        result = []
        for i in range(2**n):
            binary_str = bin(i)[2:]
            binary_str = '0' * (n - len(binary_str)) + binary_str
            if is_valid_binary_string(binary_str):
                result.append(binary_str)
        return result 
