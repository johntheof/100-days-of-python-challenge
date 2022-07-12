#len(4837) will produce an error, because function won't work with numbers
#example of right len use, prints number of characters that the user will input as a name
num_char = len(input('What is your name? '))

#Below line will produce error because of wrong Concatenation. Adding a string to an integer won't work.
#print('Your name has ' + num_char + 'characters.')

#Check what type a variable is
print(type(num_char))

#Example of how you can convert a type (type casting).
#num_char is int, in order to convert to string we do the following:
new_num_char = str(num_char)

#Now we can use the previous example with correct Concatenation of same data types.
print('Your name has ' + new_num_char + ' characters.')

#Example of mover data type conversions.

a = 123
print(type(a)) # Is integer

new_a = str(a) # Converted to a string
print(type(new_a))

new_float_a = float(a) # Converted to a float
print(70 + float("100.5")) # Does correct num calculations, since you converted a string to a float. We've converted string 100.5 to a float number. Then added 70 onto it and printed the results.

print(str(70) + str(100)) # Example of Concatenation.

