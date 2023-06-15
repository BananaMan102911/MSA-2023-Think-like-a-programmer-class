#[2,6,8,9]

date = "6/15/2023"

#get the month, day, and year values from a date
#use the .split() string method
date_parts = date.split("/")
print(date_parts)

#assign varables to the date month and year
month_number = int(date_parts[0])
day = date_parts[1]
year = date_parts[2]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#print day month and year
print(f"Day: {date_parts[1]}")
print(f"Month:{months[month_number - 1]}")
print(f"Year: {date_parts[2]}" )