import MiscFunctions 
import binascii
import base64
import os

#Cryptopals Challenge 1
def ConvertHextoBase64() :
    print(MiscFunctions.hexTobase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))


#Cryptopals Challenge 2
def FixedXOR():
    b1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    b2 = bytes.fromhex('686974207468652062756c6c277320657965')
    print(MiscFunctions.xorCombination(b1,b2).hex())



#Cryptopals Challenge 3

def SingleByteXORCipher(cipher):


    #cipher = bytes.fromhex(
    #  '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

    potential_messages = []
    for key_value in range(256):
        message = MiscFunctions.singleCharacterXOR(cipher, key_value)
        score = MiscFunctions.getEnglishScore(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value
        }
        potential_messages.append(data)
    return sorted(potential_messages,
            key=lambda x: x['score'], reverse=True)[0]
    


#Cryptopals Challenge 4

def DetectSingleByteXORString(filepath):
    ciphers = open(filepath).read().splitlines()
    potentialPlaintext = []
    for hextstring in ciphers:
        ciphertext = bytes.fromhex(hextstring)
        potentialPlaintext.append(SingleByteXORCipher(ciphertext))

    best_score = sorted(potentialPlaintext,key=lambda x:x['score'],reverse=True)[0]

    for item in best_score:
        print("{}: {}".format(item.title(), best_score[item]))

#Cryptopals Challenge 5 can be solved by using a combination of the already Created Functions

#Cryptopals Challenge 6

def BreakRepeatingKeyXOR(ciphertext):
    """ Attempts to break repeating-key XOR encryption """

    averages_distances = []

    #Take the keysize from the suggested range

    for keysize in range(1,41):
        
        #Initialize list to store Hamming Distances for this keysize
        distances = []
        

        #Break the ciphertext into chunks the lenght of the keysize

        chunks = [ciphertext[i: i +keysize] for i in range(0,len(ciphertext),keysize)]

        while True:
            try:
                #Take the two chunks at the beginning of the list
                #Get the Hamming Distance between these 2 chunks

                chunk_1 = chunks[0]
                chunk_2 = chunks[1]

                distance = MiscFunctions.calculateHammingDistance(chunk_1,chunk_2)

                #Normalize the result by dividing by the keysize

                distances.append(distance/keysize)

                #Remove these 2 chunks so when the loop starts over we get the next 2 parts of the cipher

                del chunks[0]
                del chunks[1]

                #When an exception Occurs (indicating all chunks have been processed)
                #Break the loop

            except Exception as e:                
                break

        
        result = {
            'key':keysize,
            'avg_distance' :sum(distances) / len(distances)
        }

        averages_distances.append(result)

    #Take the 5 shortest average Distances
    possible_key_lengths = sorted(averages_distances,key = lambda x: x['avg_distance'])[:5]

    possible_plaintext = []

    #Iterating through each one of the five results with the shortest
    #Normalized differences

    for res in possible_key_lengths:
        #Will populate with a single characted as each transposed
        #Block has been single byte-XOR brute forced

        key = b''

        for i in range(res['key']):

            #Create a block made up of each nth byte , where n
            #is the keysize

            block = b''

            for j in range(i,len(ciphertext),res['key']):
                block+= bytes([ciphertext[j]])
            
            key += bytes([SingleByteXORCipher(block)['key']])
            possible_plaintext.append((MiscFunctions.XORWithRepeatingKey(ciphertext,key),key))

    return max(possible_plaintext,key = lambda x :MiscFunctions.getEnglishScore(x[0]))


def main(): 
   with open("C:\\Users\\nikok\Desktop\\Web Security tutorials\\Cryptopals Challenges\\6.txt") as input_file:
       ciphertext = base64.b64decode(input_file.read())
   print(BreakRepeatingKeyXOR(ciphertext))

if __name__ == '__main__':
    main()


