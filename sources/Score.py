import os
from utils import bad_return_code, scores_file_name


def get_current_score():
    exists = os.path.isfile(scores_file_name)

    if exists:
        with open(scores_file_name, 'r') as file:
            line = file.read()
            file.close()
            return int(line)
    else:
        return int(bad_return_code)


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    current_score = int(get_current_score())

    if current_score != bad_return_code:
        with open(scores_file_name, 'w') as file:
            new_score = points_of_winning + current_score
            file.write(str(new_score))
            print(new_score)
            file.close()
    else:
        print("Couldn't read score file")
