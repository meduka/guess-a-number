import math
import random

def show_choose_screen():
    
    choose_game = input("Please choose which game you would like to play. (A)Guess what number the computer is thinking. (B)Have the computer guess a number that you think of.")
    
    if choose_game == "A" or choose_game == "a" :
    
        play_human()
        print()
        print()
   
        
    if choose_game == "B" or choose_game == "b":
    
         play_ai()
         print()
         print()



"""

PLAYER GUESS FUNCTIONS BEGIN

"""

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

def pick_number(low, high, limit):

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

def play(guess, tries):
    guess = -1
    tries = 0

    low = 1
    high = 10
    limit_calc = (math.log(high,2))
    limit = math.ceil(limit_calc)

    rand = pick_number(low, high, limit)
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)



"""

PLAYER GUESS FUNCTIONS END

"""



"""

AI GAME FUNCTIONS BEGIN

"""

# helper functions
def show_start_screen_b():
    
    print("      _,---.                  ,----.    ,-,--.    ,-,--.           ,---.             .-._                           ___                  ,----.                .=-.-. ")
    print("  _.='.'-,  \ .--.-. .-.-. ,-.--` , \ ,-.'-  _\ ,-.'-  _\        .--.'  \           /==/ \  .-._ .--.-. .-.-..-._ .'=.'\    _..---.   ,-.--` , \  .-.,.---.   /==/_ / ")
    print(" /==.'-     //==/ -|/=/  ||==|-  _.-`/==/_ ,_.'/==/_ ,_.'        \==\-/\ \          |==|, \/ /, /==/ -|/=/  /==/ \|==|  | .' .'.-. \ |==|-  _.-` /==/  `   \ |==|, |  ")
    print("/==/ -   .-' |==| ,||=| -||==|   `.-.\==\  \   \==\  \           /==/-|_\ |         |==|-  \|  ||==| ,||=| -|==|,|  / - |/==/- '=' / |==|   `.-.|==|-, .=., ||==|  |  ")
    print("|==|_   /_,-.|==|- | =/  /==/_ ,    / \==\ -\   \==\ -\          \==\,   - \        |==| ,  | -||==|- | =/  |==|  \/  , ||==|-,   ' /==/_ ,    /|==|   '='  //==/. /  ")
    print("|==|  , \_.' )==|,  \/ - |==|    .-'  _\==\ ,\  _\==\ ,\         /==/ -   ,|        |==| -   _ ||==|,  \/ - |==|- ,   _ ||==|  .=. \|==|    .-' |==|- ,   .' `--`-`   ")
    print("\==\-  ,    (|==|-   ,   /==|_  ,`-._/==/\/ _ |/==/\/ _ |       /==/-  /\ - \       |==|  /\ , ||==|-   ,   /==| _ /\   |/==/- '=' ,|==|_  ,`-._|==|_  . ,'.  .=.     ")
    print(" /==/ _  ,  //==/ , _  .'/==/ ,     /\==\ - , /\==\ - , /       \==\ _.\=\.-'       /==/, | |- |/==/ , _  .'/==/  / / , /==|   -   //==/ ,     //==/  /\ ,  ):=; :    ")
    print(" `--`------' `--`..---'  `--`-----``  `--`---'  `--`---'         `--`               `--`./  `--``--`..---'  `--`./  `--``-._`.___,' `--`-----`` `--`-`--`--'  `=`     ")
    print()
    print()
    print()
                                                                                                                                 
                                                                                                                                 
    print(".---.                                  .           .                                              . .                .    .      ")
    print("  | |                                 _|_          |                                             _|_|                |   _|_     ")
    print("  | |--. .-.    .-..-..--.--. .,-..  . |  .-..--.  |.-. .--. .-.  .    ._.--.  .  ..-..  . .--.   | |--. .-..  . .-..|--. |  .--.")
    print("  | |  |(.-'   (  (   )  |  | |   )  | | (.-'|     |-.' |  |(   )  \  /  `--.  |  (   )  | |      | |  |(   )  |(   ||  | |  `--.")
    print("  ' '  `-`--'   `-'`-''  '  `-|`-'`--`-`-'`--'     '  `-'  `-`-' `' `'   `--'  `--|`-'`--`-'      `-'  `-`-'`--`-`-`|'  `-`-'`--'")
    print("                              |                                                   ;                              ._.'            ")
    print("                              '                                                `-'                                               ")


def get_guess_b(current_low, current_high):

    guess = (current_high + current_low) // 2
    return guess 
    
    """
    Return a truncated average of current low and high.
    """
    

def pick_number_b(low, high, limit):

    print()
    print()
    print("Pick a number between " + str(low) + " and " + str(high) + ". I will try and guess your number in " + str(limit) + " tries.")
    print()
    input("When you have your number, please press enter. ")
    print()
    print()
    
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter. 
    """
    

def check_guess_b(guess, tries, limit):
    print("TRY NUMBER: " + str(tries) + " out of " + str(limit))
    print()
    response = input("Was your number " + str(guess) + "? (too high, too low, correct) ")
    print()
    print()
    
    if response == "too high" or response == "h" or response == "high" or response == "down":
        check = 1
        return check

    if response == "too low" or response == "l" or response == "low" or response == "up":
        check = -1
        return check

    if response == "correct" or response == "yes" or response == "y" or response == "yeah":
        check = 0
        return check

          
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """

def show_result_b(check, tries):
    
    if check == 0:
        print()
        print("I win! I guessed in " + str(tries) + " time(s)!")
        print()
        print()
        

    else:
        print()
        print("Dang, I lost")
        print()
              
    """
    Says the result of the game. (The computer might always win.)
  
    """

     

def play_again_b():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.casefold()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
            

def play_b(low, high, limit):
    current_low = low
    current_high = high
    check = -1
    tries = 0
    
    pick_number_b(low, high, limit)

    
    
    while check != 0 and tries < limit:
        guess = get_guess_b(current_low, current_high)
        check = check_guess_b(guess, tries, limit)
        

        if check == -1:
            # adjust current_low
            current_low = int(guess)
            
            
        elif check == 1:
            # adjust current_high
            current_high = int(guess)


        tries += 1

            
            

    show_result_b(check, tries)

def show_credits():
    print()
    print("Goodbye.")
    print()
    print("Created by Manuela Cano.")

"""

AI GAME FUNCTIONS END

"""


def play_ai():

    low = 1
    high = 10
    limit_calc = (math.log(high,2))
    limit = math.ceil(limit_calc)

    show_start_screen_b()
    play_b(low, high, limit)
    play_again_b()

    playing = True

    while playing:
        play_b(low, high, limit)
        playing = play_again_b()
        
    show_credits()




def play_human():
    
    low = 1
    high = 10
    limit_calc = (math.log(high,2))
    limit = math.ceil(limit_calc)
    
    guess = -1
    tries = 0

    show_start_screen()
    play(guess, tries)
    play_again()

    playing = True

    while playing:
        play(guess, tries)
        playing = play_again()
        
    show_credits()







show_choose_screen()
