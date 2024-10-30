# Caleb Behrman
# UWYO COSC 1010
# 10/30/24
# Lab 7
# Lab Section: 10
# Sources, people worked with, help given to: Chatgpt, for the factorial part of the code


#This code below will just prompt the person using the code to use a positive number
#There will be a lot of if, elif, or else statements just due to different stuff the user can input
while True:
    upper_bound = input("Enter a positive integer for the upper bound (or 'exit' to quit): ")
    if upper_bound.lower() == 'exit':
        break
    if upper_bound.isdigit():
        upper_bound = int(upper_bound)
        if upper_bound < 0:
            print("Please enter a positive integer.")
        else:
            factorial = 1
            for i in range(1, upper_bound + 1):
                factorial *= i
            print(f"The result of the factorial based on the given bound {upper_bound} is {factorial}")
            break
    else:
        print("That is not a valid number. Please try again.")
#I really dont know if I did that first part right, but im pretty sure that the rest of it is correct
#I had to use chatgpt for the code above because I do not know what a factorial is, so i dont know if the code is right
print("*" * 75)

#This below is just a calculator but for adding
num_sum = 0
while True:
    user_input = input("Enter numbers to sum (or type 'exit' to finish): ")
    if user_input.lower() == 'exit':
        break
    if user_input:
        if user_input[0] == '-':
            if user_input[1:].isdigit():
                num_sum -= int(user_input[1:])
            else:
                print("Invalid input. Please enter a valid number.")
        elif user_input.isdigit():
            num_sum += int(user_input)
        else:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Input cannot be empty.")

print(f"Your final sum is {num_sum}")

print("*" * 75)

#This code below serves as a calulator with more than just summing
while True:
    calculation = input("Enter a calculation (or type 'exit' to finish): ")
    if calculation.lower() == 'exit':
        break
    try:
        # Identify the operator and split operands
        for operator in ['+', '-', '*', '/', '%']:
            if operator in calculation:
                operands = calculation.replace(' ', '').split(operator)
                if len(operands) == 2 and operands[0].isdigit() and operands[1].isdigit():
                    operand1 = int(operands[0])
                    operand2 = int(operands[1])
                    if operator == '+':
                        result = operand1 + operand2
                    elif operator == '-':
                        result = operand1 - operand2
                    elif operator == '*':
                        result = operand1 * operand2
                    elif operator == '/':
                        result = operand1 / operand2 if operand2 != 0 else "Cannot divide by zero."
                    elif operator == '%':
                        result = operand1 % operand2
                    print(f"The result of {calculation} is {result}")
                    break
        else:
            print("Invalid, try again")
    except Exception as e:
        print(f"Error: {e}. Please enter a valid calculation.")
#pretty sure that i did this right too, i ran the code and it seems to work

        