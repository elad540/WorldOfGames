import random
import requests

res = requests.get('https://open.er-api.com/v6/latest/USD')
res = res.json()
rate_ils = res.get("rates").get("ILS")


def get_money_interval():
    t = (random.randint(1, 100))
    print(t)
    return t


def get_guess_from_user(diff, t):
    my_value = int(input("Please guess Your Value in Shekel: "))
    print(my_value)
    value_interval = (t - (5 - diff)) * rate_ils, (t + (5 - diff)) * rate_ils
    print(value_interval)
    if value_interval[0] < my_value < value_interval[1]:
        print("You Won")
    else:
        print("you lost")


def play(diff):
    t = get_money_interval()
    get_guess_from_user(diff, t)
