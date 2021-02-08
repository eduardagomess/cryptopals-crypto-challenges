hex_binary_table = {"0":"0000", "1":"0001", "2":"0010", "3":"0011","4":"0100",
                    "5":"0101","6":"0110","7":"0111", "8":"1000", "9":"1001",
                    "A": 1010, "B": 1011, "C":1100, "D":1101,"E":1110, "F":1111}
 
 

binary_hex_table = {"0000":0, "0001":1, "0010":2, "0011": 3,"0100":4,
                    "0101":5,"0110":6,"0111":7, "1000":8, "1001":9,
                    "1010": "A", "1011":"B", "1100":"C", "1101":"D","1110":"E", "1111":"F"}


def hexToBinary(string):
    binary_string = ""
    for caracter in string.upper():
        binary_string += str(hex_binary_table[caracter])
    return binary_string
 

def binaryToHex(string):
    binary_list = []
    for num in range(0, len(string), 4):
        binary_list.append(string[num:num+4])
    string_hex = ""

    for i in binary_list:
        string_hex += str(binary_hex_table[i]).upper()
    return string_hex
    
    
def xorString(str1, str2):
    string_xor = ""
    if len(str1) == len(str2):
        binary_string_1 = list(hexToBinary(str1))
        binary_string_2 = list(hexToBinary(str2))
        for i in range(len(binary_string_1)):
            if binary_string_1[i] == binary_string_2[i]:
                string_xor += "0"
            else:
                string_xor += "1"
        return binaryToHex(string_xor)
    raise "The strings must be equal-length"


