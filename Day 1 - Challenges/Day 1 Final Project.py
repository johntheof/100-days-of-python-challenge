#Will build a band name generator as part of Day 1 Project - Following the course 100 Days of Code: The Complete Python Pro Bootcamp for 2022
#1. Create a greeting for your program.
print('Welcome to the band name generator!')

#2. Ask the user for the city that they grew up in.
city_name = input('In which city did you grow up in? \n')

#3. Ask the user for the name of a pet.
pet_name = input('What is the name of your pet? \n')

#4. Combine the name of their city and pet and show them their band name.
band_name = city_name + ' ' + pet_name
print('Your band name is ' + band_name)


#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end