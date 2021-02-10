binary_hex_table = {"0000":0, "0001":1, "0010":2, "0011": 3,"0100":4,
                    "0101":5,"0110":6,"0111":7, "1000":8, "1001":9,
                    "1010": "A", "1011":"B", "1100":"C", "1101":"D","1110":"E", "1111":"F"}

#list to add all strings
string_list = []

#dictionary to add valid strings
valid_strings = {}

#dictionary with value in binary number
ascii_to_bin_dictionary = {}
for num in range(255):
    ascii_to_bin_dictionary[chr(num)] = "{:08b}".format(num)

#dictionary with value as a character
binary_to_scii_dictionary = {}
for num in range(255):
    binary = "{:08b}".format(num)
    binary_to_scii_dictionary[binary] = chr(num)

def singleByteXorCipher(string):
    string_length = len(bytearray.fromhex((string)))
    count = 0
    while count != string_length:
    for num in string:
        character = chr(num)
        #multiplying the character by the length of the input string
        possible_string = character * string_length 
        
        #turn possible_string into a binary string
        possible_string_binary = ""
        for charact in possible_string:
            possible_string_binary += ascii_to_bin_dictionary[charact]
            
        #turn possible_string_binary into a hex string
        binary_list = []
        for num in range(0, len(possible_string_binary), 4):
            binary_list.append(possible_string_binary[num:num+4])
        
        possible_string_hex = ""
        for num in binary_list:
            possible_string_hex += str(binary_hex_table[num]).upper()
            
        #decimal string to byte
        str1 = bytearray.fromhex(string)
        str2 = bytearray.fromhex(possible_string_hex)
         
        #xor
        output_message = ""
        for i in range(len(str1)):
            output_message += chr(str1[i] ^ str2[i])
        
        #score related to the character frequencies in English
        score = frequencie_score(output_message)
        
        information_message = {'message': output_message,'score': score}
        
        #store message information to select the one who has the high score
        possible_messages.append(information_message)
     
    return possible_messages
    
            
biggestScore((singleByteXorCipher("0e3647e8592d35514a081243582536ed3de6734059001e3f535ce6271032")))
