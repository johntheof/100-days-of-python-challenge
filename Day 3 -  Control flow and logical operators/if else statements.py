#conditional stamenets, if / else
#they w ill do either A or B
#if condition:
#   do this
#else:
#   do that

#example xercise with rollercoaster
# make a program that asks the user to add their height in cm. If height is more than 120 cm let them ride
#otherwise print that they can't

print('Welcome to the rollercoaster')
height  = int(input('What is your height in cm'))

if height > 120:
    print('You can ride the rollercoaster')
else:
    print('Sorry you are too short!')
