def decode(n):
    
    if (type(n) is str):
        conv = ""
        for i in n:
            if 65 <= ord(i) <= 90: 
                i = chr(2*64 + 27 - ord(i))
            elif 97 <= ord(i) <= 122: 
                i = chr(2*96 + 27 - ord(i))
            conv+=i
    
        return conv
    else:
        return "Input is not a string"