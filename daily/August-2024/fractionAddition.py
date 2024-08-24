import re
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions_list = re.findall(r'[+-]?\d+/\d+', expression)
        total_numerator = 0
        total_denominator = 1
        
        for fraction in fractions_list:
            current_numerator, current_denominator = map(int, fraction.split('/'))
            total_numerator = total_numerator * current_denominator + current_numerator * total_denominator
            total_denominator *= current_denominator
        
        common_divisor = gcd(abs(total_numerator), total_denominator)
        total_numerator //= common_divisor
        total_denominator //= common_divisor

        result = []
        result.append(str(total_numerator))
        result.append('/')
        result.append(str(total_denominator))
        
        return ''.join(result)
