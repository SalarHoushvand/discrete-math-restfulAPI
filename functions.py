# -----------------------------------------------------------
# This file contains all the functions for the API.
# output of each file is sending to app.py to generate
# JSON output and route to desired path.
# -----------------------------------------------------------

# ---------- Imports ----------
import itertools
import random
import math
import datasets as ds
import jsonify as js
import uuid
import matplotlib_venn as vplt
from matplotlib import pyplot as plt

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
    empty_symbol = '∅'
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
    output_json = js.question_json_maker(uuid.uuid1().hex,
        str(question) + ' A= ' + str(set1).replace('[]', '').replace('[', '{').replace(']', '}') + ' B= ' + str(set2).replace(
            '[]', '').replace('[]', '').replace('[', '{').replace(']', '}'), choices,
        choices.index(answer) + 1)

    return output_json

def ven2():
    """Venn Diagram example for 2 sets"""

    print('Venn Diagram \n')

    set1 = set(random_set())
    set2 = set(random_set())
    # # try to add elem to set until set length is less than 3
    # for x in itertools.takewhile(lambda x: len(set1) < 7, num_gen1):
    #     set1.add(x)
    # for x in itertools.takewhile(lambda x: len(set2) < 10, num_gen2):
    #     set2.add(x)
    # print('A : ' + str(set1) + ' , B : ' + str(set2))

    # length of sets for venn diagram
    a = len(set1)
    b = len(set2)
    c = len(set1.intersection(set2))
    print('Intersection : ' + str(set1.intersection(set2)))

    # Venn Diagram
    v = vplt.venn2(subsets={'10': a, '01': b, '11': c}, set_labels=('A', 'B'))
    l1 = ','.join(map(str, set1.difference(set2)))
    v.get_label_by_id('10').set_text(l1)
    l2 = ','.join(map(str, set2.difference(set1)))
    v.get_label_by_id('01').set_text(l2)
    l3 = ','.join(map(str, set2.intersection(set1)))
    v.get_label_by_id('11').set_text(l3)
    return plt


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

    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def floor_ceiling_function():
    """
    Generates floor and ceiling function with random floats and asks for the answer.

    :return: questions in JSON format.
    """
    choices = []
    while len(choices) < 4:
        r_floor_symbol = '⌋'
        l_floor_symbol = '⌊'
        r_ceiling_symbol = '⌉'
        l_ceiling_symbol = '⌈'
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

    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


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

    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


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
        question = 'what is the domain of this function ? f(x)=' + str(zip1).replace('[', '{').replace(']', '}')
        zip2 = []
        for i in zip1:
            zip2.append(i[0])
        answer = str(set(zip2))
        choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


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
        question = 'what is the domain of this function ? f(x)=' + str(zip1).replace('[', '{').replace(']', '}')
        zip2 = []
        for i in zip1:
            zip2.append(i[1])
        answer = str(set(zip2))
        choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


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
    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def event_probability_2():
    """
       Generates a question for event probability.
       :return: question, answer choices, correct answer.(JSON)
       """
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
    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def event_probability_3():
    choices = []
    while len(choices) < 4:
        a = random.randint(5, 9)
        b = random.randint(8, 12)
        question = ('While picking out a tie, you have the choice between ' + str(a) + ' satin ties or ' + str(b) +
                    ' cotton. How many tie choices do you have?')
        answer = str(a + b)
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


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
    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def multiplication_2():
    """
        Generates a question for multiplication.
        :return: question, answer choices, correct answer.(JSON)
        """
    choices = []
    while len(choices) < 4:
        a = random.randint(5, 10)
        question = ('You decide to flip a coin ' + str(a) + ' times, resulting in a sequence of heads (H) '
                                                            'or tails (T). How many difference sequences'
                                                            ' of heads and tails are possible?')
        answer = str(2 ** a)
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def multiplication_3():
    """
        Generates a question for multiplication.
        :return: question, answer choices, correct answer.(JSON)
        """
    choices = []
    while len(choices) < 4:
        a = random.randint(5, 10)
        question = ('Rolling a 3-sided die results in a 1, 2, or 3 appearing. If you roll the die ' + str(
            a) + ' times, how many different sequences are possible?')
        answer = str(3 ** a)
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def multiplication_4():
    """
        Generates a question for multiplication.
        :return: question, answer choices, correct answer.(JSON)
        """
    choices = []
    while len(choices) < 4:
        a = random.randint(4, 8)
        b = random.randint(3, 6)
        c = random.randint(4, 9)
        question = ('You have ' + str(a) + ' shirts, ' + str(b) + ' pairs of shoes, and ' + str(
            c) + ' pairs of pants. How many outfits can you make?')
        answer = str(a * b * c)
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def permutation_1():
    """
       Generates a question for event permutation.
       :return: question, answer choices, correct answer.(JSON)
    """
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

    return js.question_json_maker(uuid.uuid1().hex, question, choices, choices.index(answer) + 1)


def permutation_2():
    """
          Generates a question for event permutation.
          :return: question, answer choices, correct answer.(JSON)
       """
    choices = []

    while len(choices) < 4:
        a = random.randint(5, 8)
        word_list = ['phone', 'truck', 'beach', 'ideal', 'spare', 'smart', 'tower', 'times', 'today']
        selected_word = random.choice(word_list)
        question = f'How many different {str(a)} letter words can be made' \
            f' from {selected_word} if letters cannot be repeated?'
        answer = str((math.factorial(a)) / (math.factorial(a - (len(selected_word)))))
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def combination_1():
    """
       Generates a question for combination.
       :return: question, answer choices, correct answer.(JSON)
       """
    choices = []
    while len(choices) < 4:
        athletes_num = random.randint(3, 6)
        total_num = athletes_num + random.randint(4, 8)
        question = f'{athletes_num} are going to be selected out of a team of {total_num}' \
            f' how many posisible combinations' \
            f' exist?'
        answer = str(
            math.factorial(total_num) / (math.factorial(athletes_num - athletes_num) * math.factorial(athletes_num)))
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def combination_2():
    """
           Generates a question for combination.
           :return: question, answer choices, correct answer.(JSON)
           """
    choices = []
    while len(choices) < 4:
        a = random.randint(2, 7)
        b = random.randint(3, 8)
        question = (str(a) + ' marbles are drawn from a bag containing ' + str(a) + ' red and ' + str(
            b) + ' white marbles. How many different draws are there?')
        answer = str((math.factorial(a + b)) / (math.factorial(a) * math.factorial(b)))
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def combination_3():
    choices = []
    while len(choices) < 4:
        a = random.randint(3, 6)
        b = random.randint(20, 40)
        question = ('Drawing ' + str(a) + ' cards from a standard deck of ' + str(
            b) + ' cards, how many different card hands are there?')
        answer = str((math.factorial(b)) / (math.factorial(b - a)))
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def conditional_probability_1():
    """
          Generates a question for conditional probability.
          :return: question, answer choices, correct answer.(JSON)
          """
    choices = []
    while len(choices) < 4:

        allergic_percent = round(random.uniform(2, 8), 2)
        question = f'The {allergic_percent} percent of adults are female are allergic to sesame, ' \
            f'what is the probability of being allergic to sesame, given being a female? round your answer to nearest hundredth'
        raw_result = ((allergic_percent / 100) / (0.5)) * 100
        answer = str(round(raw_result, 2)) + '%'
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def probability_union():
    choices = []
    while len(choices) < 4:
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
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def probability_complement():
    choices = []
    while len(choices) < 4:

        possible_outcomes = [1, 2, 3, 4, 5, 6]
        chosen_ones = []
        for i in range(random.randint(1, 5)):
            chosen_ones.append(random.choice(possible_outcomes))

        excluded_numebrs = str(set(chosen_ones)).replace('[', '{').replace(']', '}')
        question = f'We are rolling a normal dice, What is the probability that out come would not be' \
            f'one of these numbers ? {excluded_numebrs} round your answer to nearest hundredth'
        chosen_ones = set(chosen_ones)
        raw_answer = (1 - (len(chosen_ones) / 6)) * 100
        answer = str(round(raw_answer, 2)) + '%'
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1)


def bayes_theorem():
    choices = []
    while len(choices) < 4:
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
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))

    return js.question_json_maker(uuid.uuid1().hex, question, choices, choices.index(answer) + 1)

# Relations ------------------------------------------

def relations_1():
    """
    Generates a question for relations.
    :return: question, answer choices, correct answer.(JSON)
    """
    choices = []
    while len(choices) < 4:
        a = random.randint(2, 5)
        question = (f'How many relations does set A have? A={random_set(integer= a)}').replace('[','{').replace(']','}')
        answer = 2**2**(a)
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(uuid.uuid1().hex, question, choices, choices.index(answer) + 1)


def is_reflexive(universe, relation):
    """
    Function to determine if a relation of a set is reflexiver
    :param universe: a set
    :param relation: a relation on set universe
    return: True if relation is a reflexiver relation of set universe
    """
    new_set = {(a, b) for a in universe for b in universe if a == b}
    if relation >= new_set:
        return True

    return False



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


def inverse_of_relation(r):
    """
    Function to determine the inverse of a relation
    :param r: a relation
    :return: inverse of the relation
    """
    return [(y,x) for (x,y) in r]

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
    for (x,y) in set([pair for pair in r if pair in inverse_of_relation(r)]):
        if x != y:
            return False
    return True


def relations_2():
    """
    Generates a question for relations.
    :return: question, answer choices, correct answer.(JSON)
    """
    choices = []
    question = 'Which of the following is a reflexive relation on set {0,1}?'
    binary_relations = [[]]
    for pair in [(1, 1), (1, 0), (0, 1), (0, 0)]:
        binary_relations = binary_relations + [L + [pair] for L in binary_relations]
    random.shuffle(binary_relations)
    universe = [0, 1]
    while len(choices) < 4:
        for i in range(len(binary_relations)):
            if is_reflexive(set(universe), set(binary_relations[i])) == True:
                answer = binary_relations[i]
                choices.append(binary_relations[i])
                break
        for i in range(len(binary_relations)):
            if is_reflexive(set(universe), set(binary_relations[i])) != True:
                choices.append(binary_relations[i])
                if len(choices) == 4:
                    break
    random.shuffle(choices)
    return js.question_json_maker(uuid.uuid1().hex, question, choices, choices.index(answer) + 1)


def relations_3():
    """
    Generates a question for relations.
    :return: question, answer choices, correct answer.(JSON)
    """
    choices = []
    question = 'Which of the following is an irreflexive relation on set {0,1}?'
    binary_relations = [[]]
    for pair in [(1,1), (1,0), (0,1), (0,0)]:
        binary_relations = binary_relations + [L + [pair] for L in binary_relations]
    random.shuffle(binary_relations)
    universe = [0,1]
    while len(choices)<4:
        for i in range(len(binary_relations)):
            if is_irreflexive(set(universe), set(binary_relations[i])) == True:
                answer = binary_relations[i]
                choices.append(binary_relations[i])
                break
        for i in range(len(binary_relations)):
            if is_irreflexive(set(universe), set(binary_relations[i])) != True:
                choices.append(binary_relations[i])
                if len(choices)==4:
                    break
    random.shuffle(choices)
    return js.question_json_maker(uuid.uuid1().hex, question, choices, choices.index(answer) + 1)


def relations_4():
    """
    Generates a question for relations.
    :return: question, answer choices, correct answer.(JSON)
    """
    choices = []
    question = 'Which of the following is a symmetric relation on set {0,1}?'
    binary_relations = [[]]
    for pair in [(1,1), (1,0), (0,1), (0,0)]:
        binary_relations = binary_relations + [L + [pair] for L in binary_relations]
    random.shuffle(binary_relations)
    universe = [0,1]
    while len(choices)<4:
        for i in range(len(binary_relations)):
            if is_symmetric(binary_relations[i]) == True:
                answer = binary_relations[i]
                choices.append(binary_relations[i])
                break
        for i in range(len(binary_relations)):
            if is_symmetric(binary_relations[i]) != True:
                choices.append(binary_relations[i])
                if len(choices)==4:
                    break
    random.shuffle(choices)
    return js.question_json_maker(uuid.uuid1().hex, question, choices, choices.index(answer) + 1)


def relations_5():
    """
    Generates a question for relations.
    :return: question, answer choices, correct answer.(JSON)
    """
    choices = []
    question = 'Which of the following is an asymmetric relation on set {0,1}?'
    binary_relations = [[]]
    for pair in [(1,1), (1,0), (0,1), (0,0)]:
        binary_relations = binary_relations + [L + [pair] for L in binary_relations]
    random.shuffle(binary_relations)
    universe = [0,1]
    while len(choices)<4:
        for i in range(len(binary_relations)):
            if is_asymmetric(binary_relations[i]) == True:
                answer = binary_relations[i]
                choices.append(binary_relations[i])
                break
        for i in range(len(binary_relations)):
            if is_asymmetric(binary_relations[i]) != True:
                choices.append(binary_relations[i])
                if len(choices)==4:
                    break
    random.shuffle(choices)
    return js.question_json_maker(uuid.uuid1().hex, question, choices, choices.index(answer) + 1)


def relations_6():
    """
    Generates a question for relations.
    :return: question, answer choices, correct answer.(JSON)
    """
    choices = []
    question = 'Which of the following is an anitsymmetric relation on set {0,1}?'
    binary_relations = [[]]
    for pair in [(1,1), (1,0), (0,1), (0,0)]:
        binary_relations = binary_relations + [L + [pair] for L in binary_relations]
    random.shuffle(binary_relations)
    universe = [0,1]
    while len(choices)<4:
        for i in range(len(binary_relations)):
            if is_antisymmetric(binary_relations[i]) == True:
                answer = binary_relations[i]
                choices.append(binary_relations[i])
                break
        for i in range(len(binary_relations)):
            if is_antisymmetric(binary_relations[i]) != True:
                choices.append(binary_relations[i])
                if len(choices)==4:
                    break
    random.shuffle(choices)
    return js.question_json_maker(uuid.uuid1().hex, question, choices, choices.index(answer) + 1)

def img_test():
    choices = []
    question = 'Which of the following is an anitsymmetric relation on set {0,1}?'
    binary_relations = [[]]
    for pair in [(1, 1), (1, 0), (0, 1), (0, 0)]:
        binary_relations = binary_relations + [L + [pair] for L in binary_relations]
    random.shuffle(binary_relations)
    universe = [0, 1]
    img = '<img src="data:image/png;base64, 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">'
    choices=[img]
    answer = img
    random.shuffle(choices)
    return js.question_json_maker(uuid.uuid1().hex, question, choices, choices.index(answer) + 1)