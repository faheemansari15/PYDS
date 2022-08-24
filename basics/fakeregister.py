username = input('Enter user username')
email = input('enter your email')
gender = input('Enter your gender')
password = input('Enter your password')
confirm_password = input('Confirm your password')


if len(username) > 4 and len(username) < 25:
    if '@' in email:
        if password == confirm_password:
            print('Registration Successfull')
        else:
            print('Password do not match')
            print('Registration Unsuccessfull')
    else:
        print('Email is invalid')
        print('Registration Unsuccessfull')
else:
     print('Username must be between 4 and 25 characters')
     print('Registration Unsuccessfull')     

# OR, we can write in this type

username = input('Enter user username')
email = input('enter your email')
gender = input('Enter your gender')
password = input('Enter your password')
confirm_password = input('Confirm your password')
msz = ''

if len(username) < 4 or len(username) > 25:
    msz += 'Username Invalid\n'
if '@' not in email:
    msz += 'Invalid Email\n'
if password != confirm_password:
    msz += 'Password does not match'
if len(msz) > 0:
    print('Error\n', msz)
else:
    print('Registration Successful')    