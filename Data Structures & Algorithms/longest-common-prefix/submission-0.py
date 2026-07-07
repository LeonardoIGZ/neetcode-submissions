class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_prefix_len = 200
        sample = ""

        for x in strs:
            if max_prefix_len > len(x):
                max_prefix_len = len(x)
                sample = x

        index = 0
        are_equals = 0

        while max_prefix_len > 0:
            prefix = strs[index]
            
            if sample[0:max_prefix_len] == prefix[0:max_prefix_len]:
                are_equals += 1
                index += 1

                if are_equals == len(strs): 
                    return sample[0:max_prefix_len]
            else:
                are_equals = 0
                index = 0
                max_prefix_len -= 1
                
        return ""
