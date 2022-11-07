# This function has a person name as an input and returns a string:
def welcome(name):
    print(f"""\033[1;34;40mHello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to
    play. \033[0m""")


# This function presents the games list and lets the user choose one of them to play:
def load_game():
    game_choose = input("""\nPlease choose a game to play:
                        \n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
                        \n2. Guess Game - guess a number and see if you chose like the computer
                        \n3. Currency Roulette - try and guess the value of a random amount of USD in ILS
""")
    return valid_num(1, 3, game_choose)


def valid_num(minimum, maximum, number):
    while True:
        if type(number) != "int":
            if number.isdigit():
                if minimum <= int(number) <= maximum:
                    return int(number)
                else:
                    number = input(f"""\033[1;31;40m Error - you must choose number between: {minimum} - {maximum}: 
                    \033[0m""")
            else:
                number = input(f"\033[1;31;40m Please enter numbers only between: {minimum} - {maximum}:\033[0m")


# This function lets the user choose the game's difficulty:
def difficulty():
    diff = input("Please choose game difficulty from 1 to 5: ")
    return valid_num(1, 5, diff)
