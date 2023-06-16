while True:
    #prompt the user for the expression
    Expression = input('what is your expression that you would like to solve? ')
    #use .split() to get the parts of the expression. split at the space
    Expression_parts = Expression.split(' ')
    #get values from the list
    first_number = int(Expression_parts[0])
    operation = Expression_parts[1]
    second_number = int(Expression_parts[2])

    answer = 0
    #Determine the type of operation to carry out. Using if/elif/else statement
    if operation == "*":
        answer = first_number * second_number
    elif operation == '+':
        answer = first_number + second_number
    elif operation == '/':
        answer = first_number / second_number
    elif operation == '-':
        answer = first_number - second_number
    
    #Run the expression and print output formatted to one decimal place

    print(f'The answer to the expression {Expression} is {answer}')


