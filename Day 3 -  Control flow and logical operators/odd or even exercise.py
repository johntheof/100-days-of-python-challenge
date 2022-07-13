#Write a program that works out whether if a given number is an odd or even number.

num = float(input(('Which number you want to check?')))
if (num % 2) == 0:
    print('Your number is even')
else:
    print('Your number is odd')