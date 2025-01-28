import random
import os
import sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the password generator!\n')

# Get required password makeup
requested_length = int(input('How long do you want your password to be in total?\n\n'))
requested_numbers = int(input(f'How many of the {requested_length} characters do you want to me numbers?\n\n'))
requested_symbols = int(input(f'How many of the {requested_length} characters do you want to me symbols?\n\n'))

password = ''

#Pick random items from each list
password_letters =  random.choices(letters,k=requested_length-requested_numbers-requested_symbols)
password_numbers =  random.choices(numbers,k=requested_numbers)
password_symbols =  random.choices(symbols,k=requested_symbols)

#Error Checking: Check that the numbers and symbols are not longer then requested_length
if requested_numbers + requested_symbols > requested_length:
    print('ERROR, you have requested more numbers and symbols then the total password length!')
    if input('Retry? Y/N:').capitalize == 'Y':
        #Restart the app
        os.execv(sys.argv[0], sys.argv)
    else:
        print('Good Bye!')
else:
    #Combine the lists
    password_selection = password_letters + password_numbers + password_symbols

    #shuffle everything up
    random.shuffle(password_selection)

    # Add each item to the password
    for i in password_selection:
        password += i

    #checking that the password has correct numbers and symbols
    total_numbers = 0
    total_symbols = 0

    for i in password:
        if i in numbers:
            total_numbers += 1
        if i in symbols:
            total_symbols += 1
        else:
            pass

    #Check that the password meets requirements
    if len(password) == requested_length and total_symbols == requested_symbols and total_numbers == requested_numbers:
        # Give password
        print(f'Your password is: {password}. \nThis password is {len(password)} characters long, has {total_numbers} numbers and {total_symbols} symbols as requested!\n')
        if input('Make another? Y/N:').capitalize == 'Y':
            #Restart the app
            os.execv(sys.argv[0], sys.argv)
    else:
        if input('Something has gone wrong! Retry? Y/N:').capitalize == 'Y':
            #Restart the app
            os.execv(sys.argv[0], sys.argv)
        else:
            pass

