class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairs = {}

        for i in range(len(nums)):
            exists = pairs.get(nums[i])
              
            if exists != None:
                return [exists, i]
            else:
                value = target - nums[i]
                pairs[value] = i

        return [0, 0]