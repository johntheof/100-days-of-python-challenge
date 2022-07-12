#I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#https://waitbutwhy.com/2014/05/life-weeks.html
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left.
#Where x, y and z are replaced with the actual calculated numbers.

age = int(input('What is your current age? '))
life_left_yrs = 90 - age
days_left = 365 * life_left_yrs
weeks_left = 52 * life_left_yrs
months_left = 12 * life_left_yrs
print(f'You have {days_left} days, {weeks_left} weeks, {months_left} months left.')