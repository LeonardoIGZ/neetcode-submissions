class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # storing values
        bucket = set(nums)

        # streak counters
        max_streak = 0
        streak = 0

        # searching max streak posible
        for num in bucket:
            if num - 1 not in bucket:
                tmp_num = num
                
                while (tmp_num in bucket):
                    streak += 1
                    tmp_num += 1
                
                max_streak = max(max_streak, streak)
                streak = 0

        return max_streak



