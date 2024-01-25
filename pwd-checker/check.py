SMALPHA = 'abcdefghijklmnopqrstuvwxyz'
CAPALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUM = '0123456789'
SPL = '!@#$%^&*()_+-=[]{}|;:,.<>/?~'
WEAK = ['123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', '111111', '1234567', 'dragon',
 '123123', 'baseball', 'abc123', 'football', 'monkey', 'letmein', '696969', 'shadow', 'master', '666666',
 'qwertyuiop', '123321', 'mustang', '1234567890', 'michael', '654321', 'pussy', 'superman', '1qaz2wsx', '7777777',
  'fuckyou', '121212', '000000', 'qazwsx', '123qwe', 'killer', 'trustno1', 'jordan', 'jennifer', 'zxcvbnm', 
  'asdfgh', 'hunter', 'buster', 'soccer', 'harley', 'batman', 'andrew', 'tigger', 'sunshine', 'iloveyou', 
  'fuckme', '2000', 'charlie', 'robert', 'thomas', 'hockey', 'ranger', 'daniel', 'starwars', 'klaster', 
  '112233', 'george', 'asshole', 'computer', 'michelle', 'jessica', 'pepper', '1111', 'zxcvbn', '555555', 
  '11111111', '131313', 'freedom', '777777', 'pass', 'fuck', 'maggie', '159753', 'aaaaaa', 'ginger', 
  'princess', 'joshua', 'cheese', 'amanda', 'summer', 'love', 'ashley', '6969', 'nicole', 'chelsea', 
  'biteme', 'matthew', 'access', 'yankees', '987654321', 'dallas', 'austin', 'thunder', 'taylor', 'matrix']
MSG = {
    -1: 'Vulnerable: Password too common',
    0: 'Very Weak: Password length lesser than 8',
    1: 'Weak: Password must have atleast one number',
    2: 'Moderate: Password must have atleast one uppercase letter',
    3: 'Good: Password must have atleast one special character',
    4: 'Strong: Password is strong'
}


def strength(password):
    # pwd must be unique
    if password in WEAK:
        return -1
    # pwd lth must be >= 8
    if len(password) < 8:
        return 0
    # pwd must have atleast one number
    elif set(password).intersection(set(NUM)) == set():
        return 1
    # pwd must have atleast one uppercase letter
    elif set(password).intersection(set(CAPALPHA)) == set():
        return 2
    # pwd must have atleast one spl char
    elif set(password).intersection(set(SPL)) == set():
        return 3
    # strong pwd
    else:
        return 4

def main():
    pin = ''
    score = 0
    while pin != '^d' and score != 4:
        pin = input('Enter password: ')
        if pin == '^d':
            break
        score = strength(pin)
        print(MSG[score])

if __name__ == '__main__':
    main()
