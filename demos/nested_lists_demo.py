#create a list
demo_list = [15, 9, 64, 25, 9, 11, 32, 41]
list_of_lists = [[2,4,7,9],
                 [3,7,8,4],
                 [1,8,5,2]]
#get data from lists
print(demo_list[2])

#print the 6 in lists of lists
print(list_of_lists[1][2])

#print all of the values in the list matriz format
for number in demo_list:
    print(number)

print("\n")
for row in range(len(list_of_lists)):
    print(list_of_lists[row])

print("\n")
#iterate over the rows
for row in range(len(list_of_lists)):
    #iterate over the colums
    print(f"\n |Row {row + 1} Values|")
    for column in range(len(list_of_lists[row])):
        print(list_of_lists[row][column])