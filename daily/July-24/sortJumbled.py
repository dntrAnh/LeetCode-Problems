class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def translate(num: int) -> int:
            num = str(num)
            new_num = []
            for i in range(len(num)): 
                digit = int(num[i])
                real_digit = mapping[digit]
                new_num.append(str(real_digit))
            return int(''.join(new_num))
        
        num_map = []
        for num in nums: 
            num_map.append((num, translate(num)))
        
        num_map.sort(key=lambda x: x[1])
        
        result = []
        for num, _ in num_map: 
            result.append(num)
        
        return result
