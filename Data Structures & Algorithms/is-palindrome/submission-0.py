import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_word = s.replace(' ', '')
        new_word = re.sub(r'[^a-zA-Z0-9]', '', new_word)

        right = len(new_word) - 1
        left = 0

        while right > left:
            if new_word[right].lower() != new_word[left].lower():
                return False
            
            right -= 1
            left += 1
            
        return True