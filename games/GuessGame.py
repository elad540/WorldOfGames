from Live import load_game
from sources.Score import add_score


# This function generates a random number
def generates_number(diff):
    import random
    generated_number = int(random.randint(1, diff))
    return generated_number


# This function lets the user choose a number
def get_guess_from_user(diff):
    user_number = input(
        f"Welcome to the game - Guess the number\nPlease guess a number between 1 to {diff}: ")
    while True:
        if user_number.isdigit() and 1 <= int(user_number) <= 3:
            print(f"\033[1;35;40mYou chose number {user_number} \033[0m")
            return user_number
        else:
            print(f"\033[1;31;40mError - choose from 1 to {diff} only\033[0m")


# This function compares the generated number to the number that the user have guessed
def compare_results(generated_number, user_number):
    return bool(generated_number == user_number)


def play(diff):
    is_equal = compare_results(generates_number(diff), get_guess_from_user(diff))
    if is_equal:
        print("Great you guessed right!")
        add_score(diff)
    else:
        print("You lost...")
