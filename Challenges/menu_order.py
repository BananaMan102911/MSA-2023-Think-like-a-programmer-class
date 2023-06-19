"""
1. Create a dictionary containing all of the items on the menu
2. Create a function that will ask the user for their item, they will then insert it
3. Run the input from the user and if it is not on the list you reprompt the user
4. Run the ask the user for another item, adding it up on a total varible that has been established
5. if the user inserts an end prompt then end the program 
"""

#Create dictionary



def main():
    
    menu_items = {"Baja Taco": 4.00,"Burrito": 7.50,"Bowl": 8.50,"Nachos": 11.00,"Quesadilla": 8.50,"Super Burrito":
               8.50,"Super Quesadilla": 9.50,"Taco": 3.00,"Tortilla Salad": 8.00}
    total = 0
    while True:
        #prompt the user for an item
        Order = input("Item: ")
        
        #detirmine if we need to end the program 
       
        
        if Order.title() == "End":
            break
        
        #determine the ordered item and add to total
        try:
            total += menu_items[Order.title()]
        except:
            continue

        #Display the total
        print(f'Total: ${total:.2f}')
main()
