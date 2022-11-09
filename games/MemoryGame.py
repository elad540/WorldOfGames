from random import randrange
from time import sleep
from sources.utils import screen_cleaner
from sources.Score import add_score


def generate_sequence(diff):
    random_numbers = []
    i = 1
    while i <= diff:
        i = i + 1
        random_numbers.append(int(randrange(1, 101)))
    print(random_numbers)
    sleep(0.7)
    screen_cleaner()


def get_list_from_user(diff):
    user_numbers = []
    print(f'Try to guess the {diff} numbers:\r')

    for i in range(diff):
        while True:
            user_input = input()
            if not user_input or not user_input.isdigit() or int(user_input) < 1:
                print(f"\033[1;31;40mError - choose only numbers, please try again\n \033[0m")
            else:
                break
        user_numbers.append(int(user_input))
    print(user_numbers)
    return user_numbers


def is_list_equal(user_numbers, random_numbers):
    if random_numbers == user_numbers:
        list_equal = True
    else:
        list_equal = False
    return list_equal


def play(diff):
    list_equal = is_list_equal(generate_sequence(diff), get_list_from_user(diff))
    if list_equal:
        print("Great you remembered right!")
        add_score(diff)
    else:
        print("You lost...")
