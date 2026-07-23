class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypted_str = []
        # print(strs)
        
        for word in strs:
            encrypted_str.append(str(len(word)) + "#" + word)  

        return "".join(encrypted_str)

    def decode(self, s: str) -> List[str]:
        # print(s)
        index = 0
        number_str = []
        decode_str = []
        
        while index < len(s):
            current_char = s[index]
            index += 1

            if current_char == '#' and len(number_str):
                number = "".join(number_str)
                # print(index)

                str_len = int(number)
                word = s[(index) : (index + str_len)]
                # print(word)
                decode_str.append(word)
                number_str.clear()
                index += str_len
            elif ord(current_char) > 47 and ord(current_char) < 58:
                number_str.append(current_char)
            elif len(number_str):
                number_str.clear()

        return decode_str