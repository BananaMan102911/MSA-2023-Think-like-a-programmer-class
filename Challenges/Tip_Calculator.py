"""
1. Ask how much was the meal
2. Ask what percentage would you like to tip
3. Calculate the tip amount
4. Display the tip amount
"""
#Set up a function that asks for the numbers
def get_numbers(prompt):
    while True:
        try:
            Meal_Amount = float(input(prompt))
            if Meal_Amount <= 0:
                print("Please enter a number larger than zero \n")
                continue
            break
        except ValueError: 
            print("Please enter a valid number")
    return Meal_Amount

def main():
    Meal_Amount = get_numbers("How much was your meal? ")
    Tip = get_numbers("What percentage would you like to tip?(Format ex. .15)")

    Tip_Amount = Meal_Amount * Tip

    print(f"Leave ${Tip_Amount}")

main()
