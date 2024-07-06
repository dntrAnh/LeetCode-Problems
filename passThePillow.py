class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        total_rounds = time // (n - 1)
        extra = time % (n - 1)

        if total_rounds % 2 == 0: 
            return extra + 1
        else: 
            return n - extra 
