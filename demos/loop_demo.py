#For loop demo
#print integers between 0 and 10
for x in range(11):
    print(x)

#print integers between 5 and 10
print("\n\n")
for x in range(5, 11):
    print(x)

#print even numbers between 0 and 10
print("\n\n")
for x in range(0,11,2):
    print(x)

#Prompt user for start and stop values
print("\n\n")
start_value = int(input("Enter start value: "))
end_value = int(input("Enter stop value: "))

for output in range(start_value, end_value + 1):
    print(output)
