#Needs to be able to do the math to solve e=mc^2
#solves for e
# c=300000000
#algorithm
#1. Establish C
C = 300000000
#2. ask for the input for the m value
M = int(input("Enter the Value for M: "))
#3. put the numbers into a math problem
output = M * C**2
#4. output the solution
print(f"The energy of your problem with a mass of {M} is {output}"  )