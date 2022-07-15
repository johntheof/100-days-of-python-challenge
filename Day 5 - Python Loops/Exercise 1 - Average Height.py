# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.



list = input('Input a list of student heights separated by space in CM.')
list = list.split(' ')
total_height = 0
for item in list:
    total_height += int(item)

number_of_students = 0
for item in list:
    number_of_students += 1

average_height = round(total_height / number_of_students)
print(f'Average height is {average_height}')