class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1

        def bit_count(n: int) -> int:
            count = 0
            while n != 0:
                count += 1
                n = n >> 1
            return count
        
        num_bits = bit_count(num)
        bitmask = (1 << num_bits) - 1
        return num ^ bitmask
