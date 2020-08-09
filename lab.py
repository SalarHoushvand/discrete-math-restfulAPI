# -----------------------------------------------------------
# This file is for testing new functions before adding them into
# main files and will be deleted after final push.
# -----------------------------------------------------------

# Graveyard =================================================

import random
import jsonify as js
import math

# In a certain population of class:
# (n)round(raw_result,2)

def multiplication_1():
    """
    Generates a question for multiplication.
    :return: question, answer choices, correct answer.(JSON)
    """
    choices = []
    while len(choices) < 4:
        a = random.randint(3, 8)
        question = ('You need to create a password ' + str(
            a) + ' characters long. You can choose letters and numbers. Repetition of letters and numbers are allowed, '
                 'and letters can be capital or lowercase. How many passwords are possible?')
        answer = 'You have 62 choices available for each of the ' + str(
            a) + ' positions since repetition is allowed.' + str(62 ** a)
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))
    return choices



print(multiplication_1())

# ===========================================================
