#ask the user if they would like to continue. if y, continue, if n end
#incorrect operator format
#X or Z are not numbers
# Expression not in correct format. Has more than 3 parts
"""
inputs: none
outputs: int(first_number), int(second_number), string(Operation)
"""
def get_valid_expression_inputs():

    while True:
        #prompt the user for the expression
        Expression = input('what is your expression that you would like to solve? (X Y Z format) ')
        #Split the expression up using .split()
        Expression_parts = Expression.split(' ')

        if len(Expression_parts) != 3:
            print('ERROR: Enter Expression in (X Y Z)format \n')
            continue
        

        #get values from the list
        try:
            first_number = int(Expression_parts[0])
            second_number = int(Expression_parts[2])
        except ValueError:
            print("ERROR: X and Z must be numbers \n")
            continue
        
        operation = Expression_parts[1]
        #test for correct operator (*, /, +, -)
        if operation not in ["+", "-", "*", "/"]:
            print("ERROR: Incorrect operator. Only (*, /, +, -) allowed. \n")
            continue

        break
    return first_number, second_number, operation

"""
Function; to evaluate funcitions
Inputs: int(first_number), int(second_number), string(operator)
outputs; answer
"""
def evaluate_expression(first_number, second_number, operation):
        if operation == "*":
            answer = first_number * second_number
        elif operation == '+':
            answer = first_number + second_number
        elif operation == '/':
            answer = first_number / second_number
        elif operation == '-':
            answer = first_number - second_number
        return answer

def main():
    while True:
        first_number, second_number, operation = get_valid_expression_inputs()
        
        answer = evaluate_expression(first_number, second_number, operation)
        #Run the expression and print output formatted to one decimal place

        print(f'The answer is {answer}')
        #Ask the user if they want to continue
        another_calculation = input('Would you like to eavaluate another expression? (y/n): ').lower()
        

        if another_calculation != "y":
            break

main()
