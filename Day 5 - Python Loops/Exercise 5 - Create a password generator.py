#create a password generator
#user will input how many letters user wants to have in password
import random
print('Welcome to the password generator.')
password = int(input('How many letters you want to have in your password? '))
symbols = input('How many symbols? ')
numbers = input('How many numbers? ')

letters = ['a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z']
symbols = ['!,#,$,%,^,&,*,(,),_,+']
numbers = ['0,1,2,3,4,5,6,7,8,9']

finalpass = ''
for char in range(1,password + 1):
    random_letters = random.choice(letters)
    finalpass += random_letters
print(finalpass)