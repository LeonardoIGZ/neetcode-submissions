class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited_words = [False] * len(strs)
        anagrams = [] 
        
        for i in range(len(strs)):
            if not visited_words[i]:
                temp_anagrams = [strs[i]]  
                for j in range(i + 1 , len(strs)):
                    if Counter(strs[i]) == Counter(strs[j]):
                        temp_anagrams.append(strs[j])
                        visited_words[j] = True
                anagrams.append(temp_anagrams)

        return anagrams

                

