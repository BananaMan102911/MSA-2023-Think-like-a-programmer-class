#reading files in python
#open the file
data_file = open("file.txt", "r")
input()
menu_item = {}
for line_of_data in data_file:
    #what do we need to do to each line of data
    # split line of data at the ", "
    keys_value = line_of_data.split(", ")
    # create an entry to the dictionary. remember to convert the price to float
    #value = float(key_values[1])
    menu_item[keys_value[0]] = float(keys_value[1])

#close file
data_file.close()
for item, price in menu_item.items():
    print(f"{item}: ${price:.2f}")
