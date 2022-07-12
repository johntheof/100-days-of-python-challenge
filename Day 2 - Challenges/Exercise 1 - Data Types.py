#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8 
two_dig_number = input('Type a two digit number ')
new_number_first = int(two_dig_number[0]) #Converting into an int otherwise it will show the sum of the string (concatenation)
new_number_second = int(two_dig_number[1]) #Converting into an int otherwise it will show the sum of the string (concatenation)
print(new_number_first + new_number_second)