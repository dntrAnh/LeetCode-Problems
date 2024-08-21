class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(k): 
            left = result = odd_count = 0 

            for right in range(len(nums)): 
                if nums[right] % 2 != 0: 
                    odd_count += 1
                
                while odd_count > k: 
                    if nums[left] % 2 != 0: 
                        odd_count -= 1
                    left += 1
                
                result += right - left + 1
            
            return result 
            
        return at_most(k) - at_most(k - 1)
