

def show_choose_screen():
    
    choose_game = input("Please choose which game you would like to play. (A)Guess what number the computer is thinking. (B)Have the computer guess a number that you think of.")

    if choose_game == "A":
    
        play_human()
   
        
    if choose_game == "B":
    
         play_ai()



   


def play_ai():

    import math

    # config
    low = 1
    high = 10
    limit_calc = (math.log(high,2))
    limit = math.ceil(limit_calc)

    # helper functions
    def show_start_screen():
            
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


    def get_guess(current_low, current_high):

        guess = (current_high + current_low) // 2
        return guess 
        
        """
        Return a truncated average of current low and high.
        """
        

    def pick_number():

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
        

    def check_guess(guess, tries, limit):
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





def play_human():
      print("human after all")





show_choose_screen()
