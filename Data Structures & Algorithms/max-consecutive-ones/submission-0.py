class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak = 0
        last_zero = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                streak = max(streak, (i - last_zero))
                last_zero = i + 1

        streak = max(streak, (len(nums) - last_zero))
        return streak
        