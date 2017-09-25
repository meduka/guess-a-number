import random
import math

# config
low = 1
high = 10
limit_calc = (math.log(high,2))
limit = math.ceil(limit_calc)

# helper functions
def show_start_screen():
    print()
    print()
    print("   GGGG  UU   UU EEEEEEE  SSSSS   SSSSS       AAA      NN   NN UU   UU MM    MM BBBBB   EEEEEEE RRRRRR  !!! !!! ")
    print("  GG  GG UU   UU EE      SS      SS          AAAAA     NNN  NN UU   UU MMM  MMM BB   B  EE      RR   RR !!! !!! ")
    print(" GG      UU   UU EEEEE    SSSSS   SSSSS     AA   AA    NN N NN UU   UU MM MM MM BBBBBB  EEEEE   RRRRRR  !!! !!!")
    print(" GG   GG UU   UU EE           SS      SS    AAAAAAA    NN  NNN UU   UU MM    MM BB   BB EE      RR  RR          ")
    print("  GGGGGG  UUUUU  EEEEEEE  SSSSS   SSSSS     AA   AA    NN   NN  UUUUU  MM    MM BBBBBB  EEEEEEE RR   RR !!! !!!")
    print()
    print()
    print()
    
def show_credits():
    print()
    print("Goodbye.")
    print()
    print("Created by Manuela Cano.")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print()
            print("You must enter a number.")
            print()

def pick_number():

    print()
    print()
    print()
    
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")

    print()
    print()

    print("You will get " + str(limit) + " tries. Good luck.")

    print()
    print()

    return random.randint(low, high)

   

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
        print()
    elif guess > rand:
        print("You guessed too high.")
        print()

def show_result(guess, rand):
    if guess == rand:
        print()
        print("You win!")
        print()
        print()
        print("/$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$ /$$        /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$")
        print("/$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  | $$| $$       /$$__  $$|__  $$__/|_  $$_/ /$$__  $$| $$$ | $$ /$$__  $$| $$")
        print("| $$  \__/| $$  \ $$| $$$$| $$| $$  \__/| $$  \ $$| $$  \ $$| $$  \__/| $$  | $$| $$      | $$  \ $$   | $$     | $$  | $$  \ $$| $$$$| $$| $$  \__/| $$")
        print("| $$      | $$  | $$| $$ $$ $$| $$ /$$$$| $$$$$$$/| $$$$$$$$| $$ /$$$$| $$  | $$| $$      | $$$$$$$$   | $$     | $$  | $$  | $$| $$ $$ $$|  $$$$$$ | $$")
        print("| $$      | $$  | $$| $$  $$$$| $$|_  $$| $$__  $$| $$__  $$| $$|_  $$| $$  | $$| $$      | $$__  $$   | $$     | $$  | $$  | $$| $$  $$$$ \____  $$|__/")
        print("| $$    $$| $$  | $$| $$\  $$$| $$  \ $$| $$  \ $$| $$  | $$| $$  \ $$| $$  | $$| $$      | $$  | $$   | $$     | $$  | $$  | $$| $$\  $$$ /$$  \ $$    ") 
        print("|  $$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$| $$  | $$|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$  | $$   | $$    /$$$$$$|  $$$$$$/| $$ \  $$|  $$$$$$/ /$$")
        print("\______/  \______/ |__/  \__/ \______/ |__/  |__/|__/  |__/ \______/  \______/ |________/|__/  |__/   |__/   |______/ \______/ |__/  \__/ \______/ |__/")
        print()
        print()
        print()
    else:
        print()
        print("You lose... The number I was thinking of was " + str(rand) + ".")
        print()
        print()

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.casefold()

        if decision == 'y' or decision == 'yes':
            return True

            print()
            print()
            print()
            
        elif decision == 'n' or decision == 'no':
            return False
        
            print()
            print()
            print()
            
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
        print()
        print()
        print()

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()

