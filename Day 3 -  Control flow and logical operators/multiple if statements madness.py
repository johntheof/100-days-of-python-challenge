# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do C

# Above example will execute ONLY ONE OF THE THREE CONDITIONS. It's either

# if condition1:
#     do A
# if condition2:
#     do B
# else:
#     do C

#If all conditions are true, then a, b and c will all be executed.
#Previous roller coaster example, but we'll also ask them if they want photos then add additional $3 on the bill so:

print('Welcome to the rollercoaster')
height  = int(input('What is your height in cm '))
bill = 0

if height >= 120:
    print('You can ride the rollercoaster')
    age = int(input('What is your age? '))
    if age < 12:
        bill = 5
        print('Child tickets are $.5')
    elif age <= 18:
        bill = 7
        print('Youth tickets are $7')
    else:
        bill = 12
        print('Adult tickets are $12.')

    wants_photo = input('Do you want a photo taken? Y or N. ')
    if wants_photo == 'Y':
        bill += 3
    
    print(f'Your final bill is {bill}$')

else:
    print('Sorry, you have to grow taller in order to ride the rollecoaster.')