class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_repeated = {}
        t_repeated = {}

        for i in s:
            s_repeated[i] = s_repeated.get(i, 0) + 1

        for i in t:
            t_repeated[i] = t_repeated.get(i, 0) + 1

        for key, value in s_repeated.items():
            if (key not in t_repeated) or (t_repeated[key] != value):
                return False

        return True
