class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_frecuency = {}

        for num in nums:
            nums_frecuency[num] = nums_frecuency.get(num, 0) + 1

        frecuent_elements = []
        for i in range(k):
            max_val = 0
            max_key = 0

            for k, v in nums_frecuency.items():
                if v > max_val:
                    max_val = v
                    max_key = k
            
            frecuent_elements.append(max_key)
            nums_frecuency.pop(max_key)

        return frecuent_elements