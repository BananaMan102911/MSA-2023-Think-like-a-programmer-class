'''
Prompt the user, you have 50 cents due
ask for a coin input
attach the value to a varible
run through a test to make sure it is valid
make the amount due = the amount due - the coin amount
'''

#make a function that will check the coin value
def is_the_coin_valid():
    while True:
        try:
            Coin_value = int(input('insert Coin: \n'))
        except ValueError:
            print('please enter a valid coin value(25,10,5,1) \n')
            continue
        if Coin_value == 25:
            break
        elif Coin_value == 10:
            break
        elif Coin_value == 5:
            break
        elif Coin_value == 1:
            break
        else:
            print('please enter a valid coin value(25,10,5,1) \n')
            continue
    return Coin_value


#once you have a valid coin, plug it into the vending machine
def insert_coin(coin, value_due):
    value_due = value_due - coin
    return value_due

#create the main function that tells the order in which the other functions operate and then it gives us the amount inputed and the amount due
def main():
    value_due = 50
    while True:
        print(f'Amount Due: {value_due}')
        coin = is_the_coin_valid()
        value_due = insert_coin(coin, value_due)
        if value_due <= 0:
            print(f"Change:{value_due - value_due - value_due}")
            break
main()
