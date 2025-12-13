import random

def createPassword(lowerLimit, upperLimit, uppercase, symbols, numeric, space):
    characters = list(range(97, 123))
    if uppercase:
        characters.extend(range(65, 91))
    if symbols:
        characters.extend(symbolRange)
    if numeric:
        characters.extend(range(48, 58))
    if space:
        characters.append(32)
    while True:
        store = list()
        length = random.randint(lowerLimit, upperLimit)
        for i in range(length):
            store.append(chr(random.choice(characters)))
        password = ''.join(store)
        print(f'New password :{password}')
        while input('Enter \'no\' to generate new password:').lower() != 'no':
            return password

def password():
    print('1. Enter your own password:')
    print('2. Create your own password:')
    choice = input('Enter choice:')
    if choice == '1':
        password = input('Enter password:')
    elif choice == '2':
        password = randomPassword()
    return password

def randomPassword():
    lower = input('Enter lower limit of password length:')
    if not lower.isdigit():
        print('Not an integer')
        return ''
    upper = input('Enter upper limit of password length:')
    if not upper.isdigit():
        print('Not an integer')
        return ''
    uppercase = True
    if input('Do you want to include uppercase letters? (Y/N):').lower() == 'n':
        uppercase = False
    symbol = True
    if input('Do you want to include symbols? (Y/N):').lower() == 'n':
        symbol = False
    number = True
    if input('Do you want to include numbers? (Y/N):').lower() == 'n':
        number = False
    space = True
    if input('Do you want to include space? (Y/N):').lower() == 'n':
        space = False
    return createPassword(lower, upper, uppercase, symbol, number, space)
        
def credential():
    portal = input('Enter portal:')
    if portal in credentials:
        print('Portal already exists.')
        return
    userId = input('Enter username:')
    passcode = password()
    if passcode == '' or portal == '' or userId == '':
        print('Credentials not stored.')
        return
    credentials[portal] = (userId, passcode)

def load():
    with open('/home/anish/pyFile/credentials.txt', 'r') as file:
        credentialText = file.read().splitlines()
        index = 0
        while index < len(credentialText):
            if credentialText[i] == '':
                index += 1
                continue
            credentials[credentialText[i]] = (credentialText[i + 1], credentialText[i + 2])
            i += 3

def save():
    with open('/home/anish/pyFie/credentials.txt', 'a') as file:
        for i in credentials:
            file.write('\n')
            file.write(i)
            file.wrwite('\n')
            file.write(credentials[i][0])
            file.write('\n')
            file.write(credentials[i][1])

def retrieveCredentials():
    portal = input('Enter portal:')
    if portal in credentials:
        print('Username :', credentials[portal][0], sep = '')
        print('Password :', credentials[portal][1], sep = '')

def allCredentials():
    for i in credentials:
        print(f'Portal :{i}')
        print(f'Username :{credentials[i][0]}')
        print(f'Password :{credentials[i][1]}')
        print()

symbolRange = list(range(33, 48))
symbolRange.extend(range(58, 65))
symbolRange.extend(range(91, 97))
symbolRange.extend(range(123, 127))
credentials = dict()

load()

while True:
    print('1. Generate random password')
    print('2. Store credentials')
    print('3. Retrieve credentials')
    print('4. View all credentials')
    print('5. Save')
    print('6. Save and quit.')
    print('7. Quit')
    choice = input('Enter choice:')
    if choice == '1':
        randomPassword()
    elif choice == '2':
        credential()
    elif choice == '3':
        retrieveCredentials()
    elif choice == '4':
        allCredentials()
    elif choice == '5':
        save()
    elif choice == '6':
        save()
        break
    elif choice == '7':
        break
    else:
        print('Invalid choice')
