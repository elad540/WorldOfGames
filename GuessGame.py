from Live import load_game


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


def compare_results(generated_number, user_number):
    return bool(generated_number == user_number)


class GuessGame:
    def play(self):
        self.generates_number()
        if compare_results(get_guess_from_user(), generates_number()):
            return True
        else:
            return False

    # This function generates a random number
    def generates_number(self):
        import random
        generated_number = int(random.randint(1, self.diff))
        return generated_number
