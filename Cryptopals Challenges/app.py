import MiscFunctions 
import binascii

#Cryptopals Challenge 1
def ConvertHextoBase64() :
    print(MiscFunctions.hexTobase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))


#Cryptopals Challenge 2
def FixecXOR():
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


def main():
    message = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b"ICE"
    print(MiscFunctions.XORWithRepeatingKey(message,key).hex())

if __name__ == '__main__':
    main()


