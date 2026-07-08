class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_prefix_len = 200

        for x in strs:
            max_prefix_len = min(max_prefix_len, len(x))

        index = 0
        are_equals = 0
        sample = strs[0]

        while max_prefix_len > 0:  
            prefix = strs[index]
            
            if sample[0:max_prefix_len] == prefix[0:max_prefix_len]:
                are_equals += 1
                index += 1

                if are_equals == len(strs): 
                    return sample[0:max_prefix_len]
            else:
                max_prefix_len -= 1
                
        return ""
