import random

# config
low = 1
high = 1000


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    pass
    
def get_guess(current_low, current_high):

    guess = (current_high + current_low) // 2
    return guess 
    
    """
    Return a truncated average of current low and high.
    """
    

def pick_number():

    print()
    print()
    print("Pick a number between " + str(low) + " and " + str(high) + ". I will try and guess your number. ")
    print()
    input("When you have your number, please press enter. ")
    print()
    print()
    
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter. [X]
    """
    

def check_guess(guess):
    print()
    response = input("Was your number " + str(guess) + "? (too high, too low, correct) ")
    print()
    print()
    
    if response == "too high":
        check = 1
        return check

    if response == "too low":
        check = -1
        return check

    if response == "correct":
        check = 0
        return check

          
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """

def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.casefold()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            # adjust current_low
            current_low = int(guess)
            
            
        elif check == 1:
            # adjust current_high
            current_high = int(guess)
            

    show_result()


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()


#end

def show_credits():
    print()
    print("Goodbye.")
    print()
    print("Created by Manuela Cano.")


