# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x= int(input('enter value for x: '))
x += 3
print(x) 
# TODO: Multiply y by 2 using the *= operator
y= int(input('enter value for y: '))
y *= 2
print(y)
# TODO: Divide x by y and store the result in a variable called 'result'
result= x / y
# TODO: Print the value of 'result'
print(result)
# ------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a= int(input('Enter value for a: '))
b= int(input('Enter value for b: ')) 
if a > b:
    print('a value is greater than b')
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
if b % 2 == 0 :
    print('b is even') 
# TODO: Create a condition that checks if c is less than or equal to a
c= int(input('Enter value c: '))
if c <= a:
    print('c is less than or equal to a')    
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = (a > b) or (b % 2 == 0) and (c <= a)
# TODO: Print the value of 'final_condition'
print(f'Final condition is {final_condition}') 
# ------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
test_score = float(input('Enter test score (0-100): '))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if test_score >= 90 and test_score <= 100:
    print('Grade: A')
elif test_score >= 80 and test_score <= 89:
    print('Grade: B')
elif test_score >= 70 and test_score <= 79:
    print('Grade: C')
elif test_score >= 60 and test_score <= 69:
    print('Grade: D')
else: 
     print('Grade: F')
# TODO: Print the grade for the given score

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input('Enter number 1: '))
num2 = float(input('Enter number 2: '))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input('Enter an operation (+, -, *, /)= ' )
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == '+' : 
    result = num1 + num2
    print(f'Result: {num1}+{num2}={result}')
elif operation == '-' :
    result = num1 - num2
    print(f'Result: {num1}-{num2}={result}')
elif operation == '*' :
    result= num1 * num2
    print(f"Result: {num1}*{num2}={result}")  
# TODO: Handle the case of division by zero
    if num2 !=0:
        result= num1 / num2
else:
    print('Error: Division by zero is INVALID')
# TODO: Print the result of the operation