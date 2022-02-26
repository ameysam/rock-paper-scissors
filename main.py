from config import MOTIONS, RULES, MOTION_REVERSE, score_board
from random import choice
from utils import time_logger


def get_user_select():
    user_selection = input("Enter your select between `r`,`s` and `p`... ")
    if user_selection in MOTIONS.keys():
        return MOTIONS[user_selection]
    get_user_select()
    

def get_system_select():
    key = choice(list(MOTIONS.keys()))
    return MOTIONS[key]


def update_score_board(result):
    if result['user'] == 3:
        score_board['user'] += 1
    else:
        score_board['system'] += 1

    return score_board

# @time_logger
def match():
    
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
            result_msg = (f"User:`{user_select}` and System:`{system_select}` and Result is Equal")
        else:
            winner_select = RULES[sum(match)]
            if user_select == winner_select:
                results['user'] += 1
                result_msg = (f"User:`{user_select}` and System:`{system_select}` and User is winner...")
            else:
                results['system'] += 1
                result_msg = (f"User:`{user_select}` and System:`{system_select}` and System is winner...")

        print(result_msg)
    else:
        update_score_board(results)
        continue_match = input("The match is finished; Do you want to continue? (y/n)")
        if continue_match == 'y':
            match()



if __name__ == "__main__":
    match()
    print(score_board)