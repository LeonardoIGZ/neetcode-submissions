class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        repeated_items = {}

        for i in range(len(s)):
            s_key = s[i]
            s_value = repeated_items.get(s[i])
            
            if s_value is None:
                repeated_items[s_key] = 1
            else:
                repeated_items[s_key] += 1

                if repeated_items[s_key] == 0:
                    repeated_items.pop(s_key)

            t_key = t[i]
            t_value = repeated_items.get(t[i])
            
            if t_value is None:
                repeated_items[t_key] = -1
            else:
                repeated_items[t_key] -= 1

                if repeated_items[t_key] == 0:
                    repeated_items.pop(t_key)

        if not repeated_items:
            return True
        else:
            return False
