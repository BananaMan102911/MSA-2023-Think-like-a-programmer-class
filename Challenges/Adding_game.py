#import the random libray
import random
#generate a random number
random_number = random.randint(0,10)

'''
1. import my random number library
2. ask the user what level of diffuculty they would like
3. use if loops to decide diffuculty based on user input, if not valid repropmt
4. as the user how many questions they want
5. run a loop for how many questions they would like
6. propmt user for the answer to the random math problem
7. compare it to the actual answer to the question and if it is the right answer say correct, if werong reprompt for an aswer up to 3 times(run a loop that runs until it reaches three in a varible, if it gets it correct it just breaks and says correct)
8. once the user has done all of the promblems we tell hem their score then end the program
'''
#Function that asks the user for the diffuculty
def Diffuculty():
    while True:
        try: 
            level_of_diffuculty = int(input("Enter diffuculty 1, 2, 3: "))
        except:
            print("Please insert a valid diffuculty, that was letter...")
            continue
        if level_of_diffuculty == 1:
            print("Wow, someone wants the easy stuff...")
            break
        elif level_of_diffuculty == 2:
            print("Right in the middle, I can respect that...")
            break
        elif level_of_diffuculty == 3:
            print("Going for the hard stuff, if you pass without a calculator, I'm impressed...")
            break
        else:
            print("Please insert a valid diffuculty, I gave you the range, it shouldn't be that hard...")
            continue
    return level_of_diffuculty

#function that asks for the number of question you would like
def how_many_questions():
    while True:
        try:
            number_of_questions = int(input("Enter number of questions 3-10: "))
        except:
            print('Please enter a valid number, that was a letter')
            continue
        if number_of_questions >= 3 and number_of_questions <=10:
            print(f"Alright, {number_of_questions} questions, let's get started...")
            break
        else:
            print("Please enter a valid number, I gave you the range, it shouldn't be that hard...")
            continue
    return number_of_questions

#Function that asks the questions
def Question_gen(number_of_questions, level_of_diffuculty):
    correct = 0
    for x in range(number_of_questions):
        tries = 3
        number1 = generate_number(level_of_diffuculty)
        number2 = generate_number(level_of_diffuculty)
        while tries > 0:
            try:
                answer = int(input(f"question {x + 1}\n{number1} + {number2} = "))
                if answer == number1 + number2:
                    print("Good job, you got it right!")
                    correct += 1
                    break
                else:
                    tries -= 1
                    random_response(tries)
                    if not tries > 0:
                        print(f"The answer to {number1} + {number2} = {number1 + number2}")
                        break
            except ValueError:
                print(f"Please put a number, not a letter. This is math not english...|tries left {tries}")
                tries -= 1
                if not tries > 0:
                    print(f"The answer to {number1} + {number2} = {number1 + number2} better luck next time...")
                    break
    return correct

def random_response(tries):
    response = random.randint(1,9)
    if response == 1:
       print(f"Seriously, come on that wasn't the right answer... |tries left {tries}") 
    elif response == 2:
        print(f"I thought that humans were supposed to be smart...|tries left {tries}")
    elif response == 3:
        print(f"That wasn't right? Come on, you can do better...|tries left {tries}")
    elif response == 4:
        print(f"You better not miss this again...|tries left {tries}")
    elif response == 5:
        print(f"Come on, my little brother can do this math...|tries left {tries}")
    elif response == 6: 
        print(f"You might want to choose some easier math...|tries left {tries}")
    elif response == 7:
        print(f"That wasn't the right answer, come on you can do better...|tries left {tries}")
    elif response == 8:
        print(f"You're a dissapointment...|tries left {tries}")
    elif response == 9:
        print(f"You definitely want some more practice...|tries left {tries}")
        
            

def generate_number(level_of_diffuculty):
    if level_of_diffuculty == 1:
        number = random.randint(0,9)
    elif level_of_diffuculty == 2:
        number = random.randint(10, 99)
    elif level_of_diffuculty == 3:
        number = random.randint(100, 999)
    return number
        


def main():
    level_of_diffuculty = Diffuculty()
    number_of_questions = how_many_questions()
    correct = Question_gen(number_of_questions, level_of_diffuculty)
    print(f"Your grade: {((correct/number_of_questions) * 100):.2f}. If you don't like it, take it again, don't just complain about it...")

main()
    
