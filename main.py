from config import MOTIONS, RULES, MOTION_REVERSE, score_board
from random import choice
from utils import time_logger


def get_user_select():
    user_selection = input("Enter your select between `r`,`s` and `p`... ")
    if user_selection not in MOTIONS.keys():
        return get_user_select()
    return MOTIONS[user_selection]
    

def get_system_select():
    key = choice(list(MOTIONS.keys()))
    return MOTIONS[key]


def update_score_board(result):
    if result['user'] == 3:
        score_board['user'] += 1
    else:
        score_board['system'] += 1

    return score_board


def play():
    
    results = {
        'user': 0,
        'system': 0,
    }

    while results['user'] != 3 and results['system'] != 3:
        user_select = get_user_select()
        system_select = get_system_select()

        match = {user_select, system_select}

        match_tuple = tuple(match)
        user_select = MOTION_REVERSE[match_tuple[0]]
        system_select = MOTION_REVERSE[match_tuple[-1]]
        
        if len(match) == 1:
            result_msg = (f"You:`{user_select}`, System:`{system_select}` => Equal")
        else:
            winner_select = RULES[sum(match)]
            if user_select == winner_select:
                results['user'] += 1
                result_msg = (f"You:`{user_select}`, System:`{system_select}` => **User**")
            else:
                results['system'] += 1
                result_msg = (f"You:`{user_select}`, System:`{system_select}` => **System**")

        print(result_msg)
    else:
        update_score_board(results)
        print(20 * "=")
        if results['user'] == 3:
            print(f"User is Winner")
        else:
            print(f"System is Winner")
        print(20 * "#", '\n')

        continue_match = input("The match is finished; Do you want to continue? (y/n)")
        if continue_match == 'y':
            play()

@time_logger
def call_play():
    play()

if __name__ == "__main__":
    call_play()
    print(f"Finaly Score Board: {score_board}")