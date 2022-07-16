# Instructions
# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# The highest score in the class is: x

input_scores = (input('Input a list of student scores: '))
input_scores = input_scores.split(' ')
print(input_scores)
current  = 0
for score in input_scores:
    score = int(score)
    if score > current:
        current = score
print(f'The highest score in class is: {current}.')