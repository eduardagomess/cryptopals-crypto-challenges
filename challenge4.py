binary_hex_table = {"0000":0, "0001":1, "0010":2, "0011": 3,"0100":4,"0101":5,"0110":6,"0111":7,"1000":8,
                    "1001":9,"1010": "A", "1011":"B", "1100":"C", "1101":"D","1110":"E", "1111":"F"}

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

#function to get the score from the frequencies rounded of the letters in English
def frequencie_score(string):
    
    frequencies = {'a': .081, 'd': .042,'e': .12,   'h': .060,'i': .060, 'l': .040,'n': .067, 'o': .075,  'r': .059,'s': .063, 't': .090, ' ': .13}
    
    scores = []
    for byte in string.lower():
        scores.append(frequencies.get((byte), 0))
    return sum(scores)

#function to get the biggest score 
def biggestScore(options_list):
    biggest_score = 0
    for information_message in options_list:
        if information_message["score"] > biggest_score:
            biggest_score = information_message["score"]
            message = information_message["message"]
            value = information_message['value']
    
    return {'message': message,'score':biggest_score,'value': value}

def singleByteXorCipher(string):
    string_length = len(bytearray.fromhex((string)))
    possible_messages = []
    for num in range(255):
        character = chr(num)
        #multiplying the character by the length of the input string
        possible_string = character * string_length 
        
        #turn possible_string into a binary string
        possible_string_binary = ""
        for charact in possible_string:
            possible_string_binary += ascii_to_bin()[charact]
            
        #turn possible_string_binary into a hex string
        binary_list = []
        for num in range(0, len(possible_string_binary), 4):
            binary_list.append(possible_string_binary[num:num+4])
        
        possible_string_hex = ""
        for num in binary_list:
            possible_string_hex += str(binary_hex()[num]).upper()
            
        #decimal string to byte
        str1 = bytearray.fromhex(string)
        str2 = bytearray.fromhex(possible_string_hex)
         
        #xor
        output_message = ""
        for i in range(len(str1)):
            output_message += chr(str1[i] ^ str2[i])
    
        #score related to the character frequencies in English
        score = frequencie_score(output_message)
        
        information_message = {'message': output_message,'score': score,'value': num}
        
        #store message information to select the one who has the high score
        possible_messages.append(information_message)
        
    return biggestScore(possible_messages)


data_file = open(r'challenge-data.txt',"r")

possible_single_character_XOR = []

for line in data_file:
    possible_single_character_XOR.append(singleByteXorCipher(line))

print(biggestScore(possible_single_character_XOR))
