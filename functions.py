# -----------------------------------------------------------
# This file contains all the functions for the API.
# output of each file is sending to app.py to generate
# JSON output and route to desired path.
# -----------------------------------------------------------

# ---------- Imports ----------
import random
import math
import datasets as ds
import jsonify as js


# ---------- Set Operations ----------
def random_set(integer=5, floats=0, char=0, country_name=0, city_name=0, male_name=0
               , female_name=0, integer_min=0, integer_max=20, integer_type='mix'
               , float_min=0, float_max=20, float_dec=2, heterogeneous=False):
    """
    Generates set with given arguments.

    :param integer: number of integers in the set.
    :param floats: number of floats in the set.
    :param char: number of characters in the set.
    :param country_name: number of country names in the set.
    :param city_name: number of city names in the set.
    :param male_name: number of different male names in the set.
    :param female_name: number of different female names in the set.
    :param integer_min: minimum to be selected for integers.
    :param integer_max: maximum to be selected for integers.
    :param integer_type: defines if the integers should be odd, even or mix.
    :param float_min: minimum to be selected for floats.
    :param float_max: maximum to be selected for floats.
    :param float_dec: number of decimal points for floats.
    :param heterogeneous: if we want repeated elements in the set or not.
    :return: main_list
    """
    main_list = []
    # Integers
    int_temp = []
    while len(int_temp) < integer:
        if heterogeneous:
            if integer_type == 'even':
                rand_int = random.randrange(integer_min, integer_max, 2)
                if rand_int not in int_temp:
                    int_temp.append(rand_int)
                    main_list.append(rand_int)
            elif integer_type == 'odd':
                rand_int = random.randrange(integer_min, integer_max, 2) + 1
                if rand_int not in int_temp:
                    int_temp.append(rand_int)
                    main_list.append(rand_int)
            else:
                rand_int = random.randrange(integer_min, integer_max)
                if rand_int not in int_temp:
                    int_temp.append(rand_int)
                    main_list.append(rand_int)
        if heterogeneous is False:
            if integer_type == 'even':
                rand_int = random.randrange(integer_min, integer_max, 2)
                int_temp.append(rand_int)
                main_list.append(rand_int)
            elif integer_type == 'odd':
                rand_int = random.randrange(integer_min, integer_max, 2) + 1
                int_temp.append(rand_int)
                main_list.append(rand_int)
            else:
                rand_int = random.randrange(integer_min, integer_max)
                int_temp.append(rand_int)
                main_list.append(rand_int)
    # floats
    float_temp = []
    while len(float_temp) < floats:
        if heterogeneous:
            rand_float = round(random.uniform(float_min, float_max), float_dec)
            if rand_float not in float_temp:
                float_temp.append(rand_float)
                main_list.append(rand_float)
        if heterogeneous is False:
            rand_float = round(random.uniform(float_min, float_max), float_dec)
            float_temp.append(rand_float)
            main_list.append(rand_float)

    # strings
    topics = [(ds.country_names, country_name), (ds.city_names, city_name),
              (ds.male_names, male_name), (ds.female_names, female_name), (ds.characters, char)]
    string_temp = []
    for i in topics:
        if heterogeneous:
            while len(string_temp) < i[1]:
                temp1 = random.choice(i[0])
                if temp1 not in string_temp:
                    string_temp.append(temp1)
                    main_list.append(temp1)
            string_temp = []

        if heterogeneous is False:
            while len(string_temp) < i[1]:
                temp1 = random.choice(i[0])
                string_temp.append(temp1)
                main_list.append(temp1)
            string_temp = []
    return main_list


def sub_sets(sset):
    """
    Function to generate subset of a given set.

    :param sset: the set that we want to get subsets.
    :return: subsets
    """
    return subsetsRecur([], sorted(sset))


def subsetsRecur(current, sset):
    if sset:
        return subsetsRecur(current, sset[1:]) + subsetsRecur(current + [sset[0]], sset[1:])
    return [current]


# DEBUG : partition and complement
def set_operation(op='union', set_1=random_set(), set_2=random_set()):
    """
    Implements different set operations on two given sets.

    :param op: type of operation we want to implement, options are:
    'union': returns union of two set.
    'intersection': returns intersection of two sets.
    'cartesian': returns cartesian product of two sets.
    'difference': returns difference of two sets.
    'symmetric_difference': returns symmetric difference of two sets.
    'partition': returns all subsets of the given set.(only gets set_1)
    'complement': returns complement from a given set. (only gets set_1 and it considers as universal set.)

    :param set_1: first set.
    :param set_2: second set.
    :return: output
    """
    global output

    # list of symbols used in the questions in HTML unicode format
    # intersection_symbol = '&cap;'
    # union_symbol = '&cup;'
    empty_symbol = '&empty;'
    # delta = '&Delta;'

    if op == 'union':
        output = str(set(set_1).union(set(set_2))).replace("'", '')

    elif op == 'intersection':
        output = str(
            set(set_1).intersection(set(set_2))).replace('set()', empty_symbol).replace("'", '')

    elif op == 'difference':
        output = str(set(set_1).difference(set(set_2))).replace('set()',
                                                                empty_symbol).replace(
            "'", '')

    elif op == 'cartesian':
        output = str([(obj1, obj2) for obj1 in set_1 for obj2 in set_2]).replace(
            '[', '').replace(']', '')

    elif op == 'symmetric_difference':
        output = str(
            set(set_1).difference(set(set_2)).union(set(set_2).difference(set(set_1)))).replace('set()',
                                                                                                empty_symbol).replace(
            "'", '')
    elif op == 'partition':
        set_2 = []
        output = str(sub_sets(set_1)).replace('[', '{').replace(']', '}')

    elif op == 'complement':
        set_2 = []
        subset_1 = []
        for i in range(len(set_1) - 2):
            subset_1.append(random.choice(set_1))
        output = 'U= ' + str(set_1).replace('[', '{').replace(']', '}') + ' ' + 'A= ' + str(set_1).replace('[',
                                                                                                           '{').replace(
            ']', '}') + ' U-A = ' + str(set(set_1) - set(subset_1)).replace('[', '{').replace(']', '}')

    return output


def choices(par, operation):
    """
    Generates choices for set operation multiple answer questions.

    :param par: type of items in each list.(str)
    :param operation: type of operation on sets.(str)
    :return: Questions.(JSON)
    """
    choices = []
    output = []
    while len(choices) < 4:
        num2 = str(par)
        if operation == 'partition':
            set2 = []
            if num2[0] == '1':
                set1 = random_set(integer=3)
            elif num2[0] == '2':
                set1 = random_set(integer=0, floats=3)
            elif num2[0] == '3':
                set1 = random_set(integer=0, char=3)
            elif num2[0] == '4':
                set1 = random_set(integer=0, country_name=3)
            elif num2[0] == '5':
                set1 = random_set(integer=0, city_name=3)
            elif num2[0] == '6':
                set1 = random_set(integer=0, male_name=3)
            elif num2[0] == '7':
                set1 = random_set(integer=0, female_name=3)
        elif operation == 'cartesian':
            if num2[0] == '1':
                set1 = random_set(integer=3)
            elif num2[0] == '2':
                set1 = random_set(integer=0, floats=3)
            elif num2[0] == '3':
                set1 = random_set(integer=0, char=3)
            elif num2[0] == '4':
                set1 = random_set(integer=0, country_name=3)
            elif num2[0] == '5':
                set1 = random_set(integer=0, city_name=3)
            elif num2[0] == '6':
                set1 = random_set(integer=0, male_name=3)
            elif num2[0] == '7':
                set1 = random_set(integer=0, female_name=3)
            if num2[1] == '1':
                set2 = random_set(integer=3)
            elif num2[1] == '2':
                set2 = random_set(integer=0, floats=3)
            elif num2[1] == '3':
                set2 = random_set(integer=0, char=3)
            elif num2[1] == '4':
                set2 = random_set(integer=0, country_name=3)
            elif num2[1] == '5':
                set2 = random_set(integer=0, city_name=3)
            elif num2[1] == '6':
                set2 = random_set(integer=0, male_name=3)
            elif num2[1] == '7':
                set2 = random_set(integer=0, female_name=3)

        else:
            if num2[0] == '1':
                set1 = random_set()
            elif num2[0] == '2':
                set1 = random_set(integer=0, floats=5)
            elif num2[0] == '3':
                set1 = random_set(integer=0, char=5)
            elif num2[0] == '4':
                set1 = random_set(integer=0, country_name=5)
            elif num2[0] == '5':
                set1 = random_set(integer=0, city_name=5)
            elif num2[0] == '6':
                set1 = random_set(integer=0, male_name=5)
            elif num2[0] == '7':
                set1 = random_set(integer=0, female_name=5)
            if num2[1] == '1':
                set2 = random_set()
            elif num2[1] == '2':
                set2 = random_set(integer=0, floats=5)
            elif num2[1] == '3':
                set2 = random_set(integer=0, char=5)
            elif num2[1] == '4':
                set2 = random_set(integer=0, country_name=5)
            elif num2[1] == '5':
                set2 = random_set(integer=0, city_name=5)
            elif num2[1] == '6':
                set2 = random_set(integer=0, male_name=5)
            elif num2[1] == '7':
                set2 = random_set(integer=0, female_name=5)
        answer = set_operation(op=operation, set_1=set1, set_2=set2)
        if answer not in choices:
            choices.append(answer)
        else:
            pass
    if operation == 'partition' or operation == 'complement':
        question = ('What is the ' + operation + ' of this set? ').replace('[]', '').replace('[', '{').replace(']', '}')
    else:
        question = ('What is the ' + operation + ' of these two sets? ').replace('_', ' ').replace('[', '{').replace(
            ']', '}')
    choices = random.sample(choices, len(choices))
    output_json = js.question_json_maker(
        str(question) + ' ' + str(set1).replace('[]', '').replace('[', '{').replace(']', '}') + ' ' + str(set2).replace(
            '[]', '').replace('[]', '').replace('[', '{').replace(']', '}'), choices,
        choices.index(answer) + 1)

    return output_json


# ---------- Functions ----------


def function(domain_set, target_set):
    """
    :param domain_set:
    :param target_set:
    :return:
    """

    if len(domain_set) == len(set(domain_set)):
        function_type = 'General function'
        if len(target_set) != len(set(target_set)):
            if len(target_set) < len(domain_set) or len(target_set) == len(domain_set):
                function_type = 'Surjective function'
            elif len(target_set) > len(domain_set) or len(target_set) == len(domain_set):
                function_type = 'Injective function'
        elif len(target_set) == len(set(target_set)) and len(domain_set) == len(target_set):
            function_type = 'Bijective function'
    else:
        function_type = 'Not function'
    return function_type


def general_function():
    """
    Generates questions for determining if a set is function or not and if so what kind.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    choices = []
    global zip

    while len(choices) < 4:
        A = []
        B = []
        # question_json = 'question ' + str(i + 1)
        for i in range(random.randint(3, 6)):
            A.append(random.randint(1, 10))
        for i in range(random.randint(3, 6)):
            B.append(random.randint(1, 10))
        zip1 = set(zip(A, B))

        question = f'Is f(x) from ' \
                       f'A = {str(set(A)).replace("[", "{").replace("]", "}")} to ' \
                       f'B = {str(set(B)).replace("[", "{").replace("]", "}")}  a function ? ' \
                       f'If so what kind of function it is ? f(x)=' + str(zip1).replace("[", "{").replace("]", "}")
        answer = function(A, B)
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(question, choices, choices.index(answer) + 1)


def floor_ceiling_function():
    """
    Generates floor and ceiling function with random floats and asks for the answer.

    :return: questions in JSON format.
    """
    choices = []
    while len(choices) < 4:
        r_floor_symbol = '&rfloor;'
        l_floor_symbol = '&lfloor;'
        r_ceiling_symbol = '&rceil;'
        l_ceiling_symbol = '&lceil;'
        A = 0

        # question_json = 'question ' + str(i + 1)
        A = round(random.uniform(-40, 40), 2)
        identifier = random.randint(0, 10)
        if identifier % 2 == 0:
            question = l_floor_symbol + str(A) + r_floor_symbol + ' ?'
            answer = str(math.floor(A))
        else:
            question = l_ceiling_symbol + str(A) + r_ceiling_symbol + ' ?'
            answer = str(math.ceil(A))
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(question, choices, choices.index(answer) + 1)

def inverse_of_function():
    """
    Generates a random function and asks for inverse of it.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    global zip
    choices = []
    while len(choices) < 4:
        A = []
        B = []
        set_len = random.randint(3, 6)
        # question_json = 'question ' + str(i + 1)
        while len(A) != set_len:
            rand_int = random.randint(1, 15)
            if rand_int not in A:
                A.append(rand_int)
        while len(B) != set_len:
            rand_int = random.randint(15, 30)
            if rand_int not in B:
                B.append(rand_int)
        zip1 = list(zip(A, B))
        zip2 = list(zip(B, A))

        question = 'What is the inverse of function f=' + str(zip1) + ' ?'
        answer = str(zip2)
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(question, choices, choices.index(answer) + 1)

def domain():
    global zip
    choices = []
    while len(choices) < 4:
        A = []
        B = []
        # question_json = 'question ' + str(i + 1)
        for i in range(random.randint(3, 6)):
            A.append(random.randint(1, 10))
        for i in range(random.randint(3, 6)):
            B.append(random.randint(11, 21))
        zip1 = list(zip(A, B))
        question = 'what is the domain of this function ? f(x)=' + str(zip1).replace('[','{').replace(']','}')
        zip2 = []
        for i in zip1:
            zip2.append(i[0])
        answer = str(set(zip2))
        choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(question, choices, choices.index(answer) + 1)


def target():
    global zip
    choices = []
    while len(choices) < 4:
        A = []
        B = []
        # question_json = 'question ' + str(i + 1)
        for i in range(random.randint(3, 6)):
            A.append(random.randint(1, 10))
        for i in range(random.randint(3, 6)):
            B.append(random.randint(11, 21))
        zip1 = list(zip(A, B))
        question = 'what is the domain of this function ? f(x)=' + str(zip1).replace('[','{').replace(']','}')
        zip2 = []
        for i in zip1:
            zip2.append(i[1])
        answer = str(set(zip2))
        choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(question, choices, choices.index(answer) + 1)


# ---------- Probabilities ----------


def event_probability_1():
    """
    Generates a question for event probability.
    :return: question, answer choices, correct answer.(JSON)
    """
    choices = []

    while len(choices) < 4:
        roll_number = random.randint(2, 6)
        outcome_num = random.randint(1, 6)
        times = random.randint(1, roll_number)

        question = f'We throw a dice for {roll_number} times what is the probability of having number {outcome_num},' \
            f' {times} times?'
        answer = f'{times}/{6 * roll_number}'
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(question, choices, choices.index(answer) + 1)


def event_probability_2():
    choices = []

    while len(choices) < 4:
        symbols = ['spades', 'hearts', 'clubs', 'diamonds']
        cards = ['Jack', 'King', 'Queen', 'Ace']
        cards_num = random.randint(2, 8)
        goal_card1 = random.randint(2, 10)
        goal_card2 = random.choice(cards)

        question = f'{cards_num} cards are randomly drawn from a deck of normal' \
            f' playing cards (52 cards) and each time ' \
            f'drawn card replaced to the deck what is the probability' \
            f' of drawing {goal_card1} of {random.choice(symbols)} and ' \
            f' {goal_card2} of {random.choice(symbols)}?'

        answer = f'1/52<sup>{cards_num}</sup>'
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(question, choices, choices.index(answer) + 1)


def permutation_1():
    choices = []
    while len(choices) < 4:
        athletes_num = random.randint(6, 10)
        question = f'{athletes_num} athletes are competing in a tournament, the first winner ' \
            f'is going to get a golden medal, ' \
            f'second is going to get a  silver and third is going to get bronze. considering ' \
            f'the chances of all athletes for all three medals are same in how many possible' \
            f' way we can distribute the medals?'
        answer = str(math.factorial(athletes_num) / math.factorial(athletes_num - 3))
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(question, choices, choices.index(answer) + 1)


def combination_1():
    choices = []
    while len(choices) < 4:
        athletes_num = random.randint(3, 6)
        total_num = athletes_num + random.randint(4, 8)
        question = f'{athletes_num} are going to be selected out of a team of {total_num}' \
            f' how many posisible combinations' \
            f'exist?'
        answer = str(
            math.factorial(total_num) / (math.factorial(athletes_num - athletes_num) * math.factorial(athletes_num)))
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(question, choices, choices.index(answer) + 1)
