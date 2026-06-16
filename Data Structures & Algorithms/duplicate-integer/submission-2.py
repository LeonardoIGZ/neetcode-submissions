class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        repeated_items = set()

        for num in nums:
            if num in repeated_items:
                return True
            else:
                repeated_items.add(num)

        return False