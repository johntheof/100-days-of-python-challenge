#build a tip calculator
#print at the beginning welcome to the tip calculator
#it will ask for an input in dollars(total bill)
#it will then ask for an input of what % tip you would like to give to the waiter. Options: 10,12 or 15. Percentage is calculated by number * % divided by 100
#it will then ask how many people will split the bill
#it will prin how much money each person has to pay in $. Limit to 2 decimal points


print('Welcome to the tip calculator')
bill = float(input('What is the total amount you have to pay $'))
tip = int(input('What % of tip you want to give to the waiter?. 10, 12 or 15?'))
people = int(input('How many people are paying?'))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f'Each person has to pay $ {final_amount}')