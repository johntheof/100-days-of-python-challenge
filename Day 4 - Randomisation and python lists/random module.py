#remember there's askpython.com where you can find more about modules

from cmath import pi
import random 
random_integer = random.randint(1, 10) # Sets a random integer anywhere from 1 to 10
print(random_integer) 

#Spliting code to individual modules. Each module is responsible for different functionality in the program.
#In complex projects, you can have different modules, where different people work on differnet modules and combine them.

#we can use our newly created module called mymodule.py in this program

import mymodule
print(mymodule.pi) #value called from mymodule.py

random_float = random.random() # prints random float between 0 and 1
print(random_float)

love_score = random.randint(1,100) 
print(f'Your love score is {love_score}')

