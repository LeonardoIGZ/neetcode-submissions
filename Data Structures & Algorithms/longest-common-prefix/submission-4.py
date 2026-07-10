class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference = strs[0]

        for i in range(len(reference)):
            for word in strs: 
                if len(word) <= i or reference[i] != word[i]:
                    return reference[:i]

        return reference[:len(reference)]