import codecs
import binascii
import matplotlib.pyplot as plt



def hexTobase64(hex):
     """Gets a hex string and transforms it to a Base64 String """    
     return codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()


def xorCombination(initial,against): 
     """Gets 2 byte strings and returns the XOR result of the first string against the second """
     #The zip() function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables   
     return bytes([b1 ^ b2 for b1,b2 in zip(initial,against)])



def singleCharacterXOR(inputBytes,charValue):
     """Receives a string of byte characters and a character value.
     XORS every byte of the array against the character and returns the result """
     outputBytes = b''
     for byte in inputBytes:
          outputBytes += bytes([byte ^ charValue])

     return outputBytes


def getEnglishScore(input_bytes):

    """Compares each input byte to a character frequency 
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language
    """

    # From https://en.wikipedia.org/wiki/Letter_frequency
    # with the exception of ' ', which was estimated .
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
         
     # Iterate over each character and make each character lowercase     
     # Change the byte value to a string, and look up the 
     # character in the character_frequencies variable. If the
     # character doesn’t exist in the dictionary, make the value 0.    
     # Add the score to the list of scores    
     # Sum and return the score
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def XORWithRepeatingKey(messageBytes,key):
     """ XORs message based on input Key , if the message's length is longer than the key , then the key will repeat"""

     outputBytes = b''
     index = 0
     for byte in messageBytes:
          outputBytes += bytes([byte ^ key[index]])
          if (index + 1) == len(key):
               index = 0
          else:
               index +=1
     return outputBytes




     




     