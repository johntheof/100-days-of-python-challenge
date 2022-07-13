# Nested example

# if condition:
#     if another condition:
#         do this
#     else:
#         do that
# else:
#     do this


#Make example that checks height and age of someomne who wants to ride the rollercoaster

# print('Welcome to the rollercoaster')
# height = int(input('Enter your height in CM '))

# if height >= 120:
#     print('You can ride the rollercoaster')
#     age = int(input('What is your age? '))
#     if age <= 18:
#         print('Please pay $7')
#     else:
#         print('Please pay $12.')
# else:
#     print('Sorry, you have to grow taller in order to ride the rollecoaster.')


# example of elif usage

# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do that

#do same example with elif

print('Welcome to the rollercoaster')
height = int(input('Enter your height in CM '))

if height >= 120:
    print('You can ride the rollercoaster')
    age = int(input('What is your age? '))
    if age < 12:
        print('Please pay $5')
    elif age <= 18:
        print('Please pay $7')
    else:
        print('Please pay $12.')
else:
    print('Sorry, you have to grow taller in order to ride the rollecoaster.')