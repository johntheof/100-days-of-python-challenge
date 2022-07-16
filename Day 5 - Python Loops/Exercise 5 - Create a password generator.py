# #create a password generator
# #user will input how many letters user wants to have in password
import random
print('Welcome to the password generator.')
input_letters = int(input('How many letters you want to have in your password? '))
input_symbols = int(input('How many symbols? '))
input_numbers = int(input('How many numbers? '))

letters = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','k','K','l','L','m','M','n','N','p','P','o','O','y','Y','u','U','x','X','z','Z','q','Q','w','W']
symbols = ['!','#','$','%','^','&','*','(',')','_','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']

password = []
for char in range(1, input_letters + 1): #after reading the code again adding comment below of what is +1
    password.append(random.choice(letters))
for char in range(1, input_symbols + 1): #basically range [1,10] prints all numbers from 1 to 9 without including 10. So adding +1, means it ranges for the whole number without skipping
    password += random.choice(symbols)
for char in range(1, input_numbers + 1):
    password += random.choice(numbers)
random.shuffle(password)
passle = ''
for char in password:
    passle += char
print(f'Your password is {passle}')