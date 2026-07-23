class Solution:

    def encode(self, strs: List[str]) -> str:        
        encrypted_str = ""

        for word in strs:
            if len(word):
                temp_str = ""

                for i in range(len(word)):
                    ord_value = str(ord(word[i]))
                    temp_str += (ord_value + ".")
                
                encrypted_str += (temp_str + "*")
            
            else:
                temp_str = ".*"
                encrypted_str += temp_str 
            
        return encrypted_str[:-1]



    def decode(self, s: str) -> List[str]:
        print(s)

        if s == "":
            return []
       
        temp_list = s.split("*")
        final_list = []

        for item in temp_list:
            new_item = item[:-1]
            word_list = new_item.split(".")
            word = "" 

            print(word_list)
            
            for n in word_list:
                if len(n):
                    ascii_val = int(n)
                    word += chr(ascii_val)
                else:
                    word += ""

            final_list.append(word)
        
        return final_list
            
