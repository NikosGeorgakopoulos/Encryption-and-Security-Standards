import hashlib

def calculateHash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def Subscribe(username,password):
    account = username + ":" + calculateHash(password)
    f = open('accounts.txt','w')
    f.write(account)
    f.close()
    print('Registration Finished')


def Login(username,password):
    f = open('accounts.txt','r')
    accountFile = f.read()
    s = accountFile.split(':')
    usernameFile = s[0]
    passwordFile = s[1]
    hashedPassword = calculateHash(password)

    if username == usernameFile and hashedPassword == passwordFile :
        print("You are authenticated")
    else:
        print("Wrong Username or Password")



def main():
    input1 = input("Enter:\n 1]To Subscribe\n 2]To Login\n Choice> ")

    if input1 == '1':
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        Subscribe(username,password)
    elif input1=='2':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        Login(username,password)
    else:
        print("INVALID CHOICE")

main()