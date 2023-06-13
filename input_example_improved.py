#prompt the user to enter 2 numbers and output the sum of the two numbers

#Algorithto an integer

#process data//

#inputs//

#1. ask the user for the first numbers
#if error occurs prompt the user to enter a correct value
while True:
    try:
        number1 =  int(input("Enter the first value: "))
        break
    except ValueError:
        print("ERROR: please enter a valid number")
#Convert string number into an integer

#2. ask the user for the second number
while True:
    try:
        number2 =  int(input("Enter the second value: "))
        break
    except ValueError:
        print("ERROR: please enter a valid number")
#Convert string number in

#3. calculate the sum of the two numbers
sum_of_numbers = number1 + number2
#output
#4. print the answer to the user
#"The answer to x + y = sum"
print(f"The answer to {number1} + {number2} is {sum_of_numbers}")
