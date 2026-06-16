class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) < 2: 
            return False
        
        bucket = {}
        
        for num in nums:
            value = bucket.get(num, 0) + 1
            bucket[num] = value

        max_value = max(bucket.values())

        if max_value > 1:
            return True
        else:
            return False
