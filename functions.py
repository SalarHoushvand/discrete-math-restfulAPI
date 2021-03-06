# -----------------------------------------------------------
# This file contains all the functions for the API.
# output of each file is sending to app.py to generate
# JSON output and route to desired path.
# Difficulty of questions can be changed from here.
# Data used in sets such as country names are selected from datasets.py
# -----------------------------------------------------------

# ---------- Imports ----------

import random
import math
import datasets as ds
import jsonify as js
import uuid
import venn_diagram as venn
import itertools


# ---------- Template ----------

def template():
    """
    Template for making questions
    :return:
    """
    # Making a list for answer answer_choices for multiple choice question.
    answer_choices = []

    # Making 4 question and adding the answer of first three to
    # the answer options and choose the last question as the main question
    while len(answer_choices) < 4:

        # TODO
        question = 'question in string'
        answer = 'whatever the answer is'
        # END TODO
        # for making a Venn diagram
        # venn.ven2(set1, set2)

        # To prevent presence duplicate answer answer_choices.
        if answer not in answer_choices:
            answer_choices.append(answer)
        # end while

    # Shuffle answer_choices
    answer_choices = random.sample(answer_choices, len(answer_choices))

    # Put the question in json format using jsonify.py
    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


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
    string_ls = [(ds.country_names, country_name), (ds.city_names, city_name),
              (ds.male_names, male_name), (ds.female_names, female_name), (ds.characters, char)]
    string_temp = []
    for i in string_ls:
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


def set_operation(op='set-union', set_1=set(random_set()), set_2=set(random_set())):
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
    empty_symbol = '∅'
    # delta = '&Delta;'

    if op == 'set-union':
        output = str(set(set_1).union(set(set_2))).replace("'", '')

    elif op == 'set-intersection':
        output = str(
            set(set_1).intersection(set(set_2))).replace('set()', empty_symbol).replace("'", '')

    elif op == 'set-difference':
        output = str(set(set_1).difference(set(set_2))).replace('set()',
                                                                empty_symbol).replace(
            "'", '')

    elif op == 'cartesian-product':
        output = str([(obj1, obj2) for obj1 in set_1 for obj2 in set_2]).replace(
            '[', '').replace(']', '')

    elif op == 'set-symmetric-difference':
        output = str(
            set(set_1).difference(set(set_2)).union(set(set_2).difference(set(set_1)))).replace('set()',
                                                                                                empty_symbol).replace(
            "'", '')
    elif op == 'set-partition':
        # make second set empty
        set_2 = []

        output = str(sub_sets(set_1)).replace('[', '{').replace(']', '}').replace('B=', '')


    return output


def set_complement():
    """
    function to generate random questions for set complement.
    :return: Questions.(JSON)
    """
    answer_choices = []
    while len(answer_choices) < 4:
        set_1 = random_set()
        subset_1 = []
        for i in range(len(set_1) - 2):
            subset_1.append(random.choice(set_1))
        question = (
            f'What is the complement of set A= {str(set(subset_1))} considering U= {str(set(set_1))} is universal set? ').replace(
            '[]',
            '').replace(
            '[', '{').replace(']', '}').replace('_', ' ').replace('[', '{').replace(
            ']', '}')
        answer = str(set(set_1) - set(subset_1)).replace('[', '{').replace(']', '}')

        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=3)


def set_theory_choices(par, operation):
    """
    Generates choices for set operation multiple answer questions.

    :param par: type of items in each list.(str)
    :param operation: type of operation on sets.(str)
    :return: Questions.(JSON)
    """
    answer_choices = []

    while len(answer_choices) < 4:
        num2 = str(par)
        if operation == 'set-partition':
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
        if operation == 'set-complement':
            answer = set_operation(op=operation, set_1=set1, set_2=set2)
        else:
            answer = set_operation(op=operation, set_1=set(set1), set_2=set(set2))
        if answer not in answer_choices:
            answer_choices.append(answer)
        else:
            pass
    if operation == 'set-complement':
        question = ('What is the ' + operation.replace('set-',
                                                       '') + ' of set A considering U is universal set? ').replace('[]',
                                                                                                                   '').replace(
            '[', '{').replace(']', '}').replace('_', ' ').replace('[', '{').replace(
            ']', '}')
    elif operation == 'set-partition':
        question = ('What is the ' + operation.replace('set-', '') + ' of this set? ').replace('[]', '').replace('[',
                                                                                                                 '{').replace(
            ']', '}') + ' A= ' + str(set(set1)).replace('[]', '').replace('[', '{').replace(
            ']', '}')
    else:
        question = ('What is the ' + operation.replace('set-', '').replace('cartesian-product',
                                                                           'cartesian product').replace(
            'set-symmetric-difference', 'symmetric difference') + ' of these two sets? ').replace('_', ' ').replace('[',
                                                                                                                    '{').replace(
            ']', '}') + ' A= ' + str(set(set1)).replace('[]', '').replace('[', '{').replace(
            ']', '}') + ' B= ' + str(set(set2)).replace(
            '[]', '').replace('[]', '').replace('[', '{').replace(']', '}')

    answer_choices = random.sample(answer_choices, len(answer_choices))
    output_json = js.question_json_maker(uuid.uuid1().hex, str(question), answer_choices, answer_choices.index(answer) + 1,
                                         difficulty=2)

    return output_json


def intersection_venn():
    """
    Generate question for sets using Venn diagram.
    :return: Question in JSON format. Venn diagram in img tag for use in HTML.
    """
    answer_choices = []

    while len(answer_choices) < 4:
        set1 = set(random_set(integer=8, floats=0, char=0, country_name=0, city_name=0, male_name=0
                              , female_name=0, integer_min=5, integer_max=20, integer_type='mix'
                              , float_min=0, float_max=20, float_dec=2, heterogeneous=False))
        set2 = set(random_set(integer=9, floats=0, char=0, country_name=0, city_name=0, male_name=0
                              , female_name=0, integer_min=1, integer_max=30, integer_type='mix'
                              , float_min=0, float_max=20, float_dec=2, heterogeneous=False))

        question = f'Which one is correct for two sets of A = {set1} B = {set2} ?'
        answer = venn.ven2(set1, set2)
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=3)


# ---------- Functions ----------


def function(domain_set, target_set):
    """
    Determine if a relation is a function and tupe of the function.

    :return: Function or not and type of the function.
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
    answer_choices = []
    global zip

    while len(answer_choices) < 4:

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
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1,
                                  difficulty=3)


def ceiling_function():
    """
    Generates ceiling function with random floats and asks for the answer.

    :return: questions in JSON format.
    """
    answer_choices = []
    while len(answer_choices) < 4:

        r_ceiling_symbol = '⌉'
        l_ceiling_symbol = '⌈'

        A = round(random.uniform(-40, 40), 2)

        question = l_ceiling_symbol + str(A) + r_ceiling_symbol + ' ?'
        answer = str(math.ceil(A))
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=3)


def floor_function():
    """
       Generates floor function with random floats and asks for the answer.

       :return: questions in JSON format.
       """

    answer_choices = []
    while len(answer_choices) < 4:
        r_floor_symbol = '⌋'
        l_floor_symbol = '⌊'

        A = round(random.uniform(-40, 40), 2)

        question = l_floor_symbol + str(A) + r_floor_symbol + ' ?'
        answer = str(math.floor(A))

        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=3)


def inverse_function():
    """
    Generates a question for inverse of a function.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    global zip
    answer_choices = []
    while len(answer_choices) < 4:
        A = []
        B = []
        set_len = random.randint(3, 6)

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
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def function_domain():
    """
    Generates a question for domain of a function.
    :return: questions in JSON format.
    """
    global zip
    answer_choices = []
    while len(answer_choices) < 4:
        A = []
        B = []

        for i in range(random.randint(3, 6)):
            A.append(random.randint(1, 10))
        for i in range(random.randint(3, 6)):
            B.append(random.randint(11, 21))
        zip1 = list(zip(A, B))
        question = 'what is the domain of this function ? f(x)=' + str(zip1).replace('[', '{').replace(']', '}')
        zip2 = []
        for i in zip1:
            zip2.append(i[0])
        answer = str(set(zip2))
        answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))
    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=3)


def function_target():
    """
        Generates a question for target of a function.
        :return: questions in JSON format.
        """
    global zip
    answer_choices = []
    while len(answer_choices) < 4:
        A = []
        B = []
        # question_json = 'question ' + str(i + 1)
        for i in range(random.randint(3, 6)):
            A.append(random.randint(1, 10))
        for i in range(random.randint(3, 6)):
            B.append(random.randint(11, 21))
        zip1 = list(zip(A, B))
        question = 'what is the target of this function ? f(x)=' + str(zip1).replace('[', '{').replace(']', '}')
        zip2 = []
        for i in zip1:
            zip2.append(i[1])
        answer = str(set(zip2))
        answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))
    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=3)


def one_to_one_function():
    """
        Generates a question for one to one function using equation with LaTex.
        :return: questions in JSON format, equations are in LaTex format and wrapped in $$ in order to be rendered with Mathjax.
        """
    answer = f'\(x+{random.randint(2, 20)}\)'
    answer_choices = [f'\(x^{random.randint(2, 6)}\)', '$${\sqrt{x} \over 2}$$', '$${\sqrt{x}}$$', answer]
    question = 'Which one of these functions is one-to-one?'

    answer_choices = random.sample(answer_choices, len(answer_choices))
    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=3)

# ---------- Probabilities ----------


def event_probability_1():
    """
    Generates a question for event probability.
    :return: question, answer choices, correct answer.(JSON)
    """
    answer_choices = []

    while len(answer_choices) < 4:
        roll_number = random.randint(2, 6)
        outcome_num = random.randint(1, 6)
        times = random.randint(1, roll_number)

        question = f'We throw a dice for {roll_number} times what is the probability of having number {outcome_num},' \
            f' {times} times?'
        answer = f'{times}/{6 * roll_number}'
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))
    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=3)


def event_probability_2():
    """
       Generates a question for event probability.
       :return: question, answer choices, correct answer.(JSON)
       """

    answer_choices = []

    while len(answer_choices) < 4:
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
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))
    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def event_probability_3():
    """
           Generates a question for event probability.
           :return: question, answer choices, correct answer.(JSON)
           """

    answer_choices = []
    while len(answer_choices) < 4:
        a = random.randint(5, 9)
        b = random.randint(8, 12)
        question = ('While picking out a tie, you have the choice between ' + str(a) + ' satin ties or ' + str(b) +
                    ' cotton. How many tie choices do you have?')
        answer = str(a + b)
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))
    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def multiplication_rule_1():
    """
    Generates a question for multiplication.
    :return: question, answer choices, correct answer.(JSON)
    """
    answer_choices = []
    while len(answer_choices) < 4:
        a = random.randint(3, 8)
        question = ('You need to create a password ' + str(
            a) + ' characters long. You can choose letters and numbers. Repetition of letters and numbers are allowed, '
                 'and letters can be capital or lowercase. How many passwords are possible?')
        answer =  str(62 ** a)
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))
    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=3)


def multiplication_rule_2():
    """
        Generates a question for multiplication.
        :return: question, answer choices, correct answer.(JSON)
        """
    answer_choices = []
    while len(answer_choices) < 4:
        a = random.randint(5, 10)
        question = ('You decide to flip a coin ' + str(a) + ' times, resulting in a sequence of heads (H) '
                                                            'or tails (T). How many difference sequences'
                                                            ' of heads and tails are possible?')
        answer = str(2 ** a)
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))
    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def multiplication_rule_3():
    """
        Generates a question for multiplication.
        :return: question, answer choices, correct answer.(JSON)
        """
    answer_choices = []
    while len(answer_choices) < 4:
        a = random.randint(5, 10)
        question = ('Rolling a 3-sided die results in a 1, 2, or 3 appearing. If you roll the die ' + str(
            a) + ' times, how many different sequences are possible?')
        answer = str(3 ** a)
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))
    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def multiplication_rule_4():
    """
        Generates a question for multiplication.
        :return: question, answer choices, correct answer.(JSON)
        """
    answer_choices = []
    while len(answer_choices) < 4:
        a = random.randint(4, 8)
        b = random.randint(3, 6)
        c = random.randint(4, 9)
        question = ('You have ' + str(a) + ' shirts, ' + str(b) + ' pairs of shoes, and ' + str(
            c) + ' pairs of pants. How many outfits can you make?')
        answer = str(a * b * c)
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))
    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def permutation_1():
    """
       Generates a question for event permutation.
       :return: question, answer choices, correct answer.(JSON)
    """
    answer_choices = []
    while len(answer_choices) < 4:
        athletes_num = random.randint(6, 10)
        question = f'{athletes_num} athletes are competing in a tournament, the first winner ' \
            f'is going to get a golden medal, ' \
            f'second is going to get a  silver and third is going to get bronze. considering ' \
            f'the chances of all athletes for all three medals are same in how many possible' \
            f' way we can distribute the medals?'
        answer = str(math.factorial(athletes_num) / math.factorial(athletes_num - 3))
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def permutation_2():
    """
          Generates a question for event permutation.
          :return: question, answer choices, correct answer.(JSON)
       """
    answer_choices = []

    while len(answer_choices) < 4:
        a = random.randint(1, 5)
        word_list = ['phone', 'truck', 'beach', 'ideal', 'spare', 'smart', 'tower', 'times', 'today']
        selected_word = random.choice(word_list)
        question = f'How many different {str(a)} letter words can be made' \
            f' from {selected_word} if letters cannot be repeated?'
        answer = str((math.factorial(5)) / (math.factorial(5-a)))
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=3)


def combination_1():
    """
       Generates a question for combination.
       :return: question, answer choices, correct answer.(JSON)
       """
    answer_choices = []
    while len(answer_choices) < 4:
        athletes_num = random.randint(3, 6)
        total_num = athletes_num + random.randint(4, 8)
        question = f'{athletes_num} are going to be selected out of a team of {total_num}' \
            f' how many posisible combinations' \
            f' exist?'
        answer = str(
            math.factorial(total_num) / (math.factorial(athletes_num - athletes_num) * math.factorial(athletes_num)))
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def combination_2():
    """
           Generates a question for combination.
           :return: question, answer choices, correct answer.(JSON)
           """
    answer_choices = []
    while len(answer_choices) < 4:
        a = random.randint(2, 7)
        b = random.randint(3, 8)
        question = (str(a) + ' marbles are drawn from a bag containing ' + str(a) + ' red and ' + str(
            b) + ' white marbles. How many different draws are there?')
        answer = str((math.factorial(a + b)) / (math.factorial(a) * math.factorial(b)))
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def combination_3():
    """
               Generates a question for combination.
               :return: question, answer choices, correct answer.(JSON)
               """
    answer_choices = []
    while len(answer_choices) < 4:
        a = random.randint(3, 6)
        b = random.randint(20, 40)
        question = ('Drawing ' + str(a) + ' cards from a standard deck of ' + str(
            b) + ' cards, how many different card hands are there?')
        answer = str((math.factorial(b)) / (math.factorial(b - a)))
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def conditional_probability_1():
    """
          Generates a question for conditional probability.
          :return: question, answer choices, correct answer.(JSON)
          """
    answer_choices = []
    while len(answer_choices) < 4:

        allergic_percent = round(random.uniform(2, 8), 2)
        question = f'The {allergic_percent} percent of adults are female are allergic to sesame, ' \
            f'what is the probability of being allergic to sesame, given being a female? round your answer to nearest hundredth'
        raw_result = ((allergic_percent / 100) / (0.5)) * 100
        answer = str(round(raw_result, 2)) + '%'
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def probability_union():
    """
               Generates a question for union of events.
               :return: question, answer choices, correct answer.(JSON)
               """
    answer_choices = []
    while len(answer_choices) < 4:
        python = (random.randint(10, 60))
        java = (random.randint(10, 50))
        both = (random.randint(10, 20))
        python_str = str(python) + '%'
        java_str = str(java) + '%'
        both_str = str(both) + '%'

        question = f'In a certain population of class:  {python_str} are familiar with Python. {java_str} are familiar with Java.  ' \
            f'{both_str} are familiar with both Python and Java.  What percent of students are familiar with either Python or Java?'
        raw_result = str((python + java) - both)
        answer = raw_result + '%'
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def probability_complement():
    """
        Generates a question for complement of events.
        :return: question, answer choices, correct answer.(JSON)
        """
    answer_choices = []
    while len(answer_choices) < 4:

        possible_outcomes = [1, 2, 3, 4, 5, 6]
        chosen_ones = []
        for i in range(random.randint(1, 5)):
            chosen_ones.append(random.choice(possible_outcomes))

        excluded_numebrs = str(set(chosen_ones)).replace('[', '{').replace(']', '}')
        question = f'We are rolling a normal dice, What is the probability that out come would not be' \
            f' one of these numbers ? {excluded_numebrs} round your answer to nearest hundredth'
        chosen_ones = set(chosen_ones)
        raw_answer = (1 - (len(chosen_ones) / 6)) * 100
        answer = str(round(raw_answer, 2)) + '%'
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


def bayes_theorem():
    """
        Generates a question for Bayes theorem.
        :return: question, answer choices, correct answer.(JSON)
            """
    answer_choices = []
    while len(answer_choices) < 4:
        A_blue = random.randint(2, 10)
        A_red = random.randint(2, 10)
        B_blue = random.randint(2, 10)
        B_red = random.randint(2, 10)
        P_blue_from_A = A_blue / (A_blue + A_red)
        P_blue_from_B = B_blue / (B_blue + B_red)
        P_bucket = 1 / 2
        P_blue = (P_blue_from_A * P_bucket) + (P_blue_from_B * P_bucket)

        question = f'We have two buckets A and B. There are {A_blue} blue pencils and {A_red} red pencils in bucket A. And ' \
            f'there are {B_blue} blue pencils and {B_red} red pencils in bucket B. If we randomly draw a blue pencil,' \
            f' what is the probability' \
            f'that pencil was from bucket A ? '
        raw_answer = ((P_blue_from_A * P_bucket) / P_blue) * 100
        answer = str(round(raw_answer, 2)) + '%'
        if answer not in answer_choices:
            answer_choices.append(answer)
    answer_choices = random.sample(answer_choices, len(answer_choices))

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer_choices.index(answer) + 1, difficulty=4)


# ---------- Relations ----------


def is_reflexive(universe, relation):
    """
    Function to determine if a relation of a set is reflexive
    :param universe: a set
    :param relation: a relation on set universe
    return: True if relation is a reflexiver relation of set universe
    """
    new_set = {(a, b) for a in universe for b in universe if a == b}
    if relation >= new_set:
        return True

    return False


def inverse_of_relation(r):
    """
    Function to determine the inverse of a relation
    :param r: a relation
    :return: inverse of the relation
    """
    return [(y, x) for (x, y) in r]


def is_symmetric(r):
    """
    Function to determine if a realtion is symmetric
    :param r: a relation
    :return: True if relation is symmetric, False otherwise
    """
    return set(r) == set([pair for pair in r if pair in inverse_of_relation(r)])


def is_asymmetric(r):
    """
    Function to determine if a realtion is asymmetric
    :param r: a relation
    :return: True if relation is asymmetric, False otherwise
    """
    return [pair for pair in r if pair in inverse_of_relation(r)] == []


def is_antisymmetric(r):
    """
    Function to determine if a realtion is antisymmetric
    :param r: a relation
    :return: True if relation is antisymmetric, False otherwise
    """
    for (x, y) in set([pair for pair in r if pair in inverse_of_relation(r)]):
        if x != y:
            return False
    return True


def binary_relations(n):
    '''Function to find all binary relations of a set n
    :param n: a python list of elements
    :return: all binary relations of set n
    '''
    cartesian = []
    for element in itertools.product(n, n):
        cartesian.append(element)
    result = [[]]
    for pair in cartesian:
        result = result + [L + [pair] for L in result]
    return result


def is_transitive(r, universe):
    """
    Function to determine if a relation is transitive
    :param r: a relation on set universe
    :param universe: a set
    :return: True if relation is transitive, False otherwise
    """
    for a in universe:
        for b in universe:
            if (a, b) in r:
                for c in universe:
                    if (b, c) in r and (a, c) not in r:
                        return False
    return True


def is_irreflexive(universe, relation):
    """
    Function to determine if a relation of a set is irreflexiver
    :param universe: a set
    :param relation: a relation on set universe
    return: True if relation is a reflexiver relation of set universe
    """
    new_set = {(a, b) for a in universe for b in universe if a == b}
    if relation >= new_set:
        return False

    return True


def transitive_closure_function(rel, universe):
    """
    Function to determine the transitive closure of a realtion
    :param rel: A list that represents a relation
    :return: The transitive closure of a relation
    """
    result = rel
    changed = True
    while changed:
        changed = False
        for a in universe:
            for b in universe:
                for c in universe:
                    if (a, b) in result and (b, c) in result and (a, c) not in result:
                        result.append((a, c))
                        changed = True
    return result


def symmetric_closure_function(rel):
    """
    Function to determine the symmetric closure of a relation
    :param rel: A list that represents a relation
    :return: The symmetric closure of relation rel
    """
    return rel + [(y, x) for (x, y) in rel if (y, x) not in rel]


def reflexive_closure_function(rel, universe):
    """
    Function to return the reflexive closure of a relation on a set
    :param rel: A list that is a relation on set universe
    :param universe: A list that represents a set
    :return: A list that is the  relexive closure of the relation rel on the set universe
    """
    return rel + [(x, x) for x in universe if (x, x) not in rel]


# ----- Questions ------


def reflexive_relation():
    """
    A T/F question for reflexive relation/
    :return: True or False
    """
    global choices
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_reflexive(set(rand_set), set(relations[i])) != True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R a reflecive relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                    '{').replace(
            ']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_reflexive(set(rand_set), set(relations[i])) == True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R a reflecive relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                    '{').replace(
            ']', '}')
        choices = [True, False]

    return js.question_json_maker(uuid.uuid1().hex, question, choices, answer, question_type='TF', difficulty=3)

def irreflexive_relation():
    """
     A T/F question for irreflexive relation/
    :return: True or False

    """
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_irreflexive(set(rand_set), set(relations[i])) != True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R an irreflecive relation of set A? A = {rand_set}, R = {ind_relation}').replace(
            '[', '{').replace(']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_irreflexive(set(rand_set), set(relations[i])) == True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R an irreflecive relation of set A? A = {rand_set}, R = {ind_relation}').replace(
            '[', '{').replace(']', '}')

    answer_choices = [True, False]

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer, question_type='TF', difficulty=3)


def symmetric_relation():
    """
     A T/F question for symmetric relation/
    :return: True or False
    """
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_symmetric(relations[i]) != True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R a symmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                    '{').replace(
            ']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_symmetric(relations[i]) == True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R a symmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                    '{').replace(
            ']', '}')

    answer_choices = [True, False]

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer, question_type='TF', difficulty=3)


def asymmetric_relation():
    """
     A T/F question for assymetric relation/
    :return: True or False
    """
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        rand_set = [1, 3, 9]
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_asymmetric(relations[i]) != True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R an asymmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace(
            '[', '{').replace(']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_asymmetric(relations[i]) == True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R an asymmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace(
            '[', '{').replace(']', '}')

    answer_choices = [True, False]

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer, question_type='TF', difficulty=3)




def antisymmetric_relation():
    """
     A T/F question for anti symetric relation/
    :return: True or False
    """
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_antisymmetric(relations[i]) != True:
                ind_relation = relations[i]
                break
        question = (
            f'Is the relation R an antisymmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                 '{').replace(
            ']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_antisymmetric(relations[i]) == True:
                ind_relation = relations[i]
                break
        question = (
            f'Is the relation R an antisymmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                 '{').replace(
            ']', '}')

    answer_choices = [True, False]

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer, question_type='TF', difficulty=3)


def transitive_relation():
    """
    A T/F question for transitive relation/
    :return: True or False
    """
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if not is_transitive(relations[i], rand_set):
                ind_relation = relations[i]
                break
        question = f'Is the relation R a transitive relation of set A? A = {rand_set}, R = {ind_relation}'.replace(
            '[', '{').replace(']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_transitive(relations[i], rand_set):
                ind_relation = relations[i]
                break
        question = f'Is the relation R a transitive relation of set A? A = {rand_set}, R = {ind_relation}'.replace(
            '[', '{').replace(']', '}')

    answer_choices = [True, False]

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer, question_type='TF', difficulty=3)



def reflexive_closure():
    """
    A T/F question for transitive relation/
    :return: True or False
    """

    question_type = random.randint(0, 1)
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 4))))
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = relations[random.randint(1, len(relations) - 1)]
        question = (
            f'Is {closure_relation} the reflexive closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')
    if question_type == 1:
        answer = True
        rand_set = [1, 3, 9]
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = reflexive_closure_function(relation_1, rand_set)
        question = (
            f'Is {closure_relation} the reflexive closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')

    answer_choices = [True, False]

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer, question_type='TF', difficulty=3)


def symmetric_closure():
    """
    A T/F question for symmetric closure/
    :return: True or False

    """
    question_type = random.randint(0, 1)
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 4))))
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = relations[random.randint(1, len(relations) - 1)]
        question = (
            f'Is {closure_relation} the symmetric closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')
    if question_type == 1:
        answer = True
        rand_set = [1, 3, 9]
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = symmetric_closure_function(relation_1)
        question = (
            f'Is {closure_relation} the symmetric closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')

    answer_choices = [True, False]

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer, question_type='TF', difficulty=3)


def transitive_closure():
    """
    A T/F question for transitive closure/
    :return: True or False
    """
    question_type = random.randint(0, 1)
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 4))))
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = relations[random.randint(1, len(relations) - 1)]
        question = (
            f'Is {closure_relation} the transitive closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')
    if question_type == 1:
        answer = True
        rand_set = [1, 3, 9]
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = transitive_closure_function(relation_1, rand_set)
        question = (
            f'Is {closure_relation} the transitive closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')

    answer_choices = [True, False]

    return js.question_json_maker(uuid.uuid1().hex, question, answer_choices, answer, question_type='TF', difficulty=3)



