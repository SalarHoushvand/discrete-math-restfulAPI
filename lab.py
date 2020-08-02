# -----------------------------------------------------------
# This file is for testing new functions before adding them into
# main files and will be deleted after final push.
# -----------------------------------------------------------

# Graveyard =================================================

import random
import jsonify as js
import math


# (n) athletes are competing in a tournament, the first winner is going to get a golden medal, second is going to get a
# silver and third is going to get bronze. considering the chances of all athletes for all three medals are same in
# how many possible way we can distribute the medals?
# n!/n-3!

def permutations():
    athletes_num = random.randint(6, 10)
    question = f'{athletes_num} athletes are competing in a tournament, the first winner is going to get a golden medal, ' \
        f'second is going to get a  silver and third is going to get bronze. considering ' \
        f'the chances of all athletes for all three medals are same in how many possible way we can distribute the medals?'
    answer = str(math.factorial(athletes_num) / math.factorial(athletes_num - 3))
    output = question + answer
    return output


print(permutations())

# ===========================================================
