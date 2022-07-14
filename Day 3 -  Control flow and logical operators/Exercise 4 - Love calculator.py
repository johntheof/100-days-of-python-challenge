# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

print('Welcome to the love calculator')
your_name=input('What is your name? ')
your_name_lower=your_name.lower()
other_name=input('What is their name? ')
other_name_lower=other_name.lower()
combined_name= your_name_lower + other_name_lower

true_counter = str(combined_name.count('t') + combined_name.count('r') + combined_name.count('u') + combined_name.count('e'))
love_counter = str(combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e'))
final_counter_str = true_counter + love_counter
final_counter = int(final_counter_str)

if final_counter < 10 or final_counter > 90:
    print(f'Your love score is {final_counter}, you go together like coke and mentos.')
elif final_counter >= 40 and final_counter <= 50:
    print(f'Your love score is {final_counter}, you are alright together.')
else:
    print(f'Your score is {final_counter}.')