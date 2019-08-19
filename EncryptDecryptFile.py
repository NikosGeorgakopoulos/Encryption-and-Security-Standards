def save_file(result,filepath):
    #Open the File path
    f = open(filepath,'w')

    #Write the Result of the decryption
    f.write(result)


def open_file(filePath):
    #Create File Object
    f = open(filePath,'r')
    #Read File Contents
    fileContents = f.read()
    #Close File Object
    f.close()

    return fileContents


def calculateKey(key):
    results = 0
    counter = 0
    #Convert each character into an INT and add it to the results

    for char in key:
        counter +=1
        results += ord(char)

    #return the results divided by the number of charactes in the Key
    return int (results / counter)


def decrypt(filepath,key):
     #Get the encrypted Text Data

    fileContents = open_file(filepath)
    #Calculate the Key
    keyCalc = calculateKey(key)
    decResults = ''

    for line in fileContents:
        for wrd in line:
            for char in wrd:
                #Subtract from the Key Results
                intChar = ord (char) - keyCalc
                #Append the Results
                decResults+= chr (intChar)
    save_file(decResults,filepath)
    print('Finished Decryption')



def encrypt(filepath,key):
    #Get Clear Text Data

    fileContents = open_file(filepath)
    #Calculate the Key
    keyCalc = calculateKey(key)
    encResults = ''

    for line in fileContents:
        for wrd in line:
            for char in wrd:
                #Add to the Key Results
                intChar = ord (char) + keyCalc
                encResults+= chr (intChar)

    save_file(encResults,filepath)
    print('Finished Encryption')

def main():
    print("Please choose one of the following : \n 1]Encrypt \n 2]Decrypt")

    choice = input('> ')
    print("Enter the File Path :")
    filePath = input('> ')
    print ("Enter the Secret Key")
    key = input('> ')

    #Encrypt
    if choice == '1':
        encrypt(filePath,key)

    #Decrypt
    elif choice == '2':
        decrypt(filePath,key)

    else:
        print("Invalid Choice")

if  __name__ == '__main__':
    main()
