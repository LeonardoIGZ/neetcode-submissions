class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairs = {}

        for i, num in enumerate(nums):
            exists = pairs.get(num)
              
            if exists is not None:
                return [exists, i]
                
            pairs[target - num] = i

        # return None, this will never be reached beacuse the problem guarantee always a pair
        return [0]