# -----------------------------------------------------------
# This file is for testing new functions before adding them into
# main files and will be deleted after final push.
# -----------------------------------------------------------

# Graveyard =================================================

import random
import jsonify as js
import math
import functions as functions

# In a certain population of class:
# (n)round(raw_result,2)

def relations_1():
    """
    Generates a question for multiplication.
    :return: question, answer choices, correct answer.(JSON)
    """
    choices = []
    while len(choices) < 4:
        a = random.randint(2, 5)
        question = (f'How many relations does set A have? A={functions.random_set(integer= a)}')
        answer = 2**2**(a)
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))
    return choices



print(relations_1())

# ===========================================================
