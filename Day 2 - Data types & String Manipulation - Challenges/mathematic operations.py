#Most basic are + , - , * and /
print(6/3) # Division returns float always by default

#There's also ** , which raises number to a power
print(2**3)

#When there's one or more operations, there's a certain level of priority. PEMDAS in order (1. Parenthesis () , 2. Exponents ** , 3. Multiplication * , 4. Division / , 5. Addition + , 6. Subtraction - )
# When there's equal of importance operations, like multiplication & division, first will be executed what is on the left in order
# Example 2 * 8 /6 , first will have 2 * 8 executed because of the 'leftness'.

print(3 * 3 + 3 / 3 - 3) # First we'll get 3 * 3 which is 9. Then you have ( 9 + 3 / 3 - 3), next in order is division. So (9 + 1 - 3). Final result is 7.