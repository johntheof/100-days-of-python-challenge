print(round(8/3)) # Typical rounding of a number
print(round(8/3,5)) # Rounds to decimal places, in our case round(X/Y, <number-of-decimal-places)
print(8 // 3) #Removes all decimals, returns integer. Single / returns float, even on clean division (4/2 as an example).

#another example
score = 0

#User scores a point
score += 1 # Adds +1 to score. Shortcut instead of writing score = score +1
print(score)

#Same as above can do with -= , /= , *= 
score -= 1
print(score)
score *= 1
print(score)
score /= 1
print(score)

#Learning FStrings
bet = 1
#print('your school is ' + bet)  - Produces an error, because string + int
print('your school is ' + str(bet))

#more convenient way of doing shit with different data types
lego = 0 #Integer
height = 1.8 #FLoat
isWinning = True #Boolean
#Let's mix all of em, turn to string and print it out. Instead of converting all those separately then we'll use fstring
#just add character f infront of string
print(f'your score is {score}') # Did all converting without doing additional work.
#more examples
print(f'your score is {score}, your height is {height}, you are winning is {isWinning}' )