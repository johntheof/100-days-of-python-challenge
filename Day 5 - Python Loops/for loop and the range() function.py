#for number in rage(a, b):
#   print(number)
for number in range(1, 10):
    print(number)
#prints all numbers from 1 to 10, not including 10 (so 1 to 9)
print('----------')
#range also takes step size
for number in range(1, 10, 3):
    print(number)
print('----------')
#how can we add all numbers from 1 to 100 with using code
value = 0
for number in range (1, 101):
    value += number
print(value)