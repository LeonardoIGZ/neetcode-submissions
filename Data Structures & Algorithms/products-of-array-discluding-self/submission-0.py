class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_side = [1]
        right_product = 1 
        left_side = [1]
        left_product = 1

        for i in range(len(nums) - 1):
            right_product *= nums[(len(nums) - 1) - i]
            right_side.append(right_product)

            left_product *= nums[i]
            left_side.append(left_product)
        
        array_result = []
        for i in range(len(nums)):
            product = left_side[i] * right_side[(len(nums) - 1) - i]
            array_result.append(product)

        return array_result
            