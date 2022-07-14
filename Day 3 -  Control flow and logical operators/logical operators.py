# If/Else  basic
# if condition:
#     do this
# else:
#     do that


# Logical operators
# A and B -- both have to be true for the entire line of code to be true. If one of them is true only then the overall line evaluates as false 
# C or D -- either has to be true (one of the conditions) for line to be executed
# not E --  reverses a condition - if condition is false then becomes true, and vice versa

a = 12
print(not a > 15) ## a = 12 , 12 > 15 is false. Using not, reverses false into true

# Previous rollercoaster example

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
    elif age >= 45 and age <= 55: #Added example of logical operator.
        print('Mid-age tickets are free')
    else:
        bill = 12
        print('Adult tickets are $12.')

    wants_photo = input('Do you want a photo taken? Y or N. ')
    if wants_photo == 'Y':
        bill += 3
    
    print(f'Your final bill is {bill}$')

else:
    print('Sorry, you have to grow taller in order to ride the rollecoaster.')