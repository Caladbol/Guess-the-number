# Simple number guessing game!

# Modules
import math
import random
import os

# Handler
cls = lambda: os.system('cls' if os.name=='nt' else 'clear') #clear the terminal

def init():
    cls()
    init.guess_range = input("Select the range (100 or 1000): ")

    while init.guess_range != "100" and init.guess_range != "1000":
        init.guess_range = input("Please insert a valid range: ")
    
    else:
        init.guess_range = int(init.guess_range)
        init.tries = math.ceil(math.log(init.guess_range, 2))
        print("Selected range from 0 to " + str(init.guess_range))
        print("You have " + str(init.tries) + " tries.")
        
# Core game processing
def play():
    init()
    secret_num = random.randrange(0, init.guess_range)
    print(secret_num)
    
    # Game rules and answer checking
    guess = input("Guess the secret number!: ")
    try:
        guess.isdigit()
        while int(guess) != secret_num:
            if init.tries > 0:
                init.tries -= 1
                if int(guess) > secret_num:
                    print("Lower! You have ", init.tries, " tries left.")
                else:
                    print("Higher! You have ", init.tries, " tries left.")
                guess = input("Try again: ")
            else:
                print("You lost! The secret number was ", secret_num, ". Better luck next time!")
                break
        else:
            print("Contratulations, you found the secret number!")
    except:    
        guess = input("Enter a valid number!: ")

play()