#build a tip calculator
#print at the beginning welcome to the tip calculator
#it will ask for an input in dollars(total bill)
#it will then ask for an input of what % tip you would like to give to the waiter. Options: 10,12 or 15. Percentage is calculated by number * % divided by 100
#it will then ask how many people will split the bill
#it will prin how much money each person has to pay in $. Limit to 2 decimal points

print('Welcome to the tip calculator')
total = float(input('What is the total amount you have to pay $'))
tip_percentage = int(input('What % of tip you want to give to the waiter?. 10, 12 or 15?'))
people = int(input('How many people are paying?'))

total_tip = float((total * (tip_percentage / 100)))

total_tip_per_person = round(total_tip / people ,2)


print(f'Eeach person should pay ${total_tip_per_person} as tip')