MOTIONS = {
    'r': 1, 
    'p': 2, 
    's': 4
    }

MOTION_REVERSE = {v: k for k, v in MOTIONS.items()}

RULES = {
    3: 'p',
    5: 'r',
    6: 's',
}

score_board = {
    'user': 0,
    'system': 0,
}

RULES_ = {
    ('r', 'p'): 'p',
    ('r', 's'): 'r',
    ('p', 's'): 's',
}

