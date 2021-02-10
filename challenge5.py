def binary_hex():
    
    binary_hex_table = {"0000":0, "0001":1, "0010":2, "0011": 3,"0100":4,
                    "0101":5,"0110":6,"0111":7, "1000":8, "1001":9,
                    "1010": "A", "1011":"B", "1100":"C", "1101":"D","1110":"E", "1111":"F"}
    
    return binary_hex_table

#function to create a dictionary with value in binary number
def ascii_to_bin():
    ascii_to_bin_dictionary = {}
    for num in range(255):
        ascii_to_bin_dictionary[chr(num)] = "{:08b}".format(num)
    return ascii_to_bin_dictionary

#function to create adictionary with value as a character
def binary_to_scii():
    binary_to_scii_dictionary = {}
    for num in range(255):
        binary = "{:08b}".format(num)
        binary_to_scii_dictionary[binary] = chr(num)
    return binary_to_scii_dictionary

#function to format string in hex   
def formartHex(string):    
    string_binary = ""
    
    for charact in string:
        string_binary += ascii_to_bin()[charact]           
   
    binary_list = []
    for num in range(0, len(string_binary), 4):
        binary_list.append(string_binary[num:num+4])
      
    string_hex = ""
    for num in binary_list:
        string_hex += str(binary_hex()[num]).upper()
        
    return string_hex

#function to encrypt string
def encryptString(string, key_to_encrypt):
    
    string_encrypted = ''
    count_key_index = 0

    for letter in string:
        key = key_to_encrypt[count_key_index]
        count_key_index  +=1
        string_encrypted  += chr(ord(letter) ^ ord(key))
        if count_key_index == len(key_to_encrypt):
            count_key_index = 0
    
    return formartHex(string_encrypted)
                  
encryptString("""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal""", "ICE")
