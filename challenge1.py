hex_binary_table = {"0":"0000", "1":"0001", "2":"0010", "3":"0011","4":"0100",
                    "5":"0101","6":"0110","7":"0111", "8":"1000", "9":"1001",
                    "A": 1010, "B": 1011, "C":1100, "D":1101,"E":1110, "F":1111}


dec_base64_table = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N',
 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'a',
 27: 'b', 28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n',
 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't', 46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y',
 51: 'z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63:"/"}

def conversionDecToBase64(string):
      
    #string conversion from hexadecimal to binary
    binary_string = ""
    for caracter in string.upper():
        binary_string += str(hex_binary_table[caracter])
  

    #turns the binary number into a list
    binary_list = []
    for num in range(0, len(binary_string), 6):
        binary_list.append(binary_string[num:num+6])
   
    #table to convert binary number to decimal
    binary_decimal_table = {} 

    for num in range(127):
        binary = "{:06b}".format(num)
        binary_decimal_table[binary] = num

    #convert binary number to decimal and create a decimal list
    decimal_list =[]

    for binary_num in binary_list:
        if len(binary_num) < 6:
            add_equal = 6 - len(binary_num)
            decimal_num = str(binary_num) + ("=" * add_equal)
            decimal_list.append(decimal_num)
        else:
            decimal_list.append((binary_decimal_table[binary_num]))
   
    #convert decimal number to base64
    base64_string = ""       
    for dec_num in decimal_list:
        if "=" in str(dec_num):
            base64_string += dec_num
        else:
            base64_string += dec_base64_table[dec_num]
   
    return base64_string
