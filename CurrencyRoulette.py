import random
import requests


# For given difficulty d, and total value of money the interval will be: (t - (5 - d), t + (5 - d))
def get_money_interval(diff):
    url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=2e015e19466c486dc19f"
    response = requests.get(url)
    data = response.json()
    ils_rate = data['USD_ILS']
    random_num = int(random.randint(1, 101))
    t = random_num * ils_rate

    return random_num, t, round(t - (5 - diff), 2), round(t + (5 - diff), 2)


# A method to prompt a guess from the user to enter a guess of value to a given amount of USD
def get_guess_from_user(random_num):
    while True:
        try:
            guess = int(input(f"Guess the value of {random_num}$ in ILS: "))
        except ValueError:
            print("\033[1;31;40mError - choose only numbers\033[0m")
            continue
        return guess


# This function will call the functions above and play the game. Will return True / False if the user lost or won.
def play(low, high, guess):
    print("""In this game the currency of 1 USD in NIS will be presented. The computer will generate a number of USD.\n
    All you need to do is to guess what is the value of the number after the conversion""")
    get_money_interval()
    get_guess_from_user()
    if low <= guess <= high:
        return True
    else:
        return False
