class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        repeated_items = {}

        for char_s, char_t in zip(s, t):
            repeated_items[char_s] = repeated_items.get(char_s, 0) + 1            
                          
            if not repeated_items[char_s]:
                repeated_items.pop(char_s)

            repeated_items[char_t] = repeated_items.get(char_t, 0) - 1
                
            if not repeated_items[char_t]:
                repeated_items.pop(char_t)

        if not repeated_items:
            return True
        else:
            return False
