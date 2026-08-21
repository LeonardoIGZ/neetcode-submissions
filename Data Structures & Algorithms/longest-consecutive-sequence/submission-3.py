class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        bucket = set()

        # storing values
        for i in range(len(nums)):
            if not nums[i] in bucket:
                bucket.add(nums[i])

        # streak
        max_streak = 0
        streak = 0

        for num in bucket:
            if num - 1 not in bucket:
                tmp_num = num
                
                while (tmp_num in bucket):
                    streak += 1
                    tmp_num += 1
                
                max_streak = max(max_streak, streak)
                streak = 0

        return max_streak



