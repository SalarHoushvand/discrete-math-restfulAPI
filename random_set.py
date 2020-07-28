import random
import datasets as ds
import itertools
import jsonify as js


# datasets are lists made for names and characters


def random_set(integer=5, float=0, char=0, country_name=0, city_name=0, male_name=0
               , female_name=0, integer_min=0, integer_max=20, integer_type='mix'
               , float_min=0, float_max=20, float_dec=2, heterogeneous=False):
    """
    Generates set with given arguments.

    :param integer: number of integers in the set.
    :param float: number of floats in the set.
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
    while len(float_temp) < float:
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
    # intersection_symbol = u'\u2229'
    # union_symbol = u'\u222a'
    # empty_symbol = u'\u2205'
    # delta = u'\u0394'

    intersection_symbol = '&cap;'
    union_symbol = '&cup;'
    empty_symbol = '&empty;'
    delta = '&Delta;'
    set1 = str(set_1).replace("'", '').replace("[", '(').replace(']', ')')
    set2 = str(set_2).replace("'", '').replace("[", '(').replace(']', ')')
    if op == 'union':
        output = str(set(set_1).union(set(set_2))).replace("'", '').replace("{", '(').replace('}', ')')
        answer = str(set(set_1).union(set(set_2))).replace("'", '').replace("{", '(').replace('}', ')')

    elif op == 'intersection':
        output = str(
            set(set_1).intersection(set(set_2))).replace('set()', empty_symbol).replace("'", '').replace("{",
                                                                                                         '(').replace(
            '}', ')')
        # answer = str(set(set_1).intersection(set(set_2))).replace('set()', empty_symbol).replace("'", '').replace("{",
    #                                                                                                           '(').replace(
    #      '}', ')')

    elif op == 'difference':
        output = str(set(set_1).difference(set(set_2))).replace('set()',
                                                                empty_symbol).replace(
            "'", '').replace("{", '(').replace('}', ')')
        answer = str(set(set_1).difference(set(set_2))).replace('set()', empty_symbol).replace("'", '').replace("{",
                                                                                                                '(').replace(
            '}', ')')

    elif op == 'cartesian':
        output = str([(obj1, obj2) for obj1 in set_1 for obj2 in set_2]).replace(
            '[', '').replace(']', '')
        answer = str(set(set_1).difference(set(set_2))).replace('set()', empty_symbol).replace("'", '').replace("{",
                                                                                                                '(').replace(
            '}', ')')

    elif op == 'symmetric_difference':
        output = str(
            set(set_1).difference(set(set_2)).union(set(set_2).difference(set(set_1)))).replace('set()',
                                                                                                empty_symbol).replace(
            "'", '').replace("{",
                             '(').replace(
            '}', ')')

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


def function(A, B):
    output = ''
    if len(A) == len(set(A)):
        output = ('General function')
        if len(B) != len(set(B)):
            if len(B) < len(A) or len(B) == len(A):
                output = ('Surjective function')
            elif len(B) > len(A) or len(B) == len(A):
                output = ('Injective function')
        elif len(B) == len(set(B)) and len(A) == len(B):
            output = ('Bijective function')
    else:
        output = ('Not function')
    return output


def choices(par, operation):
    choices = []
    output = []
    while len(choices) < 4:
        num2 = str(par)
        if operation == 'partition':
            set2 = []
            if num2[0] == '1':
                set1 = random_set(integer=3)
            elif num2[0] == '2':
                set1 = random_set(integer=0, float=3)
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
                set1 = random_set(integer=0, float=3)
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
                set2 = random_set(integer=0, float=3)
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
                set1 = random_set(integer=0, float=5)
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
                set2 = random_set(integer=0, float=5)
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
        question = ('What is the ' + operation + ' of this set? ').replace('[]', '')
    else:
        question = ('What is the ' + operation + ' of these two sets? ').replace('_', ' ')
    choices = random.sample(choices, len(choices))
    output_json = js.json_maker(str(question) + ' ' + str(set1) + ' ' + str(set2).replace('[]', ''), choices,
                                choices.index(answer) + 1)

    return output_json


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
        question = 'what is the domain of this function ? f(x)=' + str(zip1)
        zip2 = []
        for i in zip1:
            zip2.append(i[0])
        answer = str(set(zip2))
        choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.json_maker(question, choices, choices.index(answer) + 1)


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
        question = 'what is the domain of this function ? f(x)=' + str(zip1)
        zip2 = []
        for i in zip1:
            zip2.append(i[1])
        answer = str(set(zip2))
        choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.json_maker(question, choices, choices.index(answer) + 1)


def event_probability1():
    choices = []

    while len(choices) < 4:
        roll_number = random.randint(2, 6)
        outcome_num = random.randint(1, 6)
        times = random.randint(1, roll_number)

        question = f'We throw a dice for {roll_number} times what is the probability of having number {outcome_num}, {times} times?'
        answer = f'{times}/{6 * roll_number}'
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.json_maker(question, choices, choices.index(answer) + 1)

def event_probability2():
    choices = []

    while len(choices) < 4:
        symbols = ['spades', 'hearts', 'clubs', 'diamonds']
        cards=['Jack', 'King', 'Queen', 'Ace']
        cards_num = random.randint(2,8)
        goal_card1 = random.randint(2,10)
        goal_card2= random.choice(cards)

        question = f'{cards_num} cards are randomly drawn from a deck of normal playing cards (52 cards) and each time drawn card replaced to the deck what is the probability of drawing {goal_card1} of {random.choice(symbols)} and ' \
            f' {goal_card2} of {random.choice(symbols)}?'

        answer = f'1/52<sup>{cards_num}</sup>'
        if answer not in choices:
            choices.append(answer)
    choices = random.sample(choices, len(choices))
    return js.json_maker(question, choices, choices.index(answer) + 1)

print(event_probability2())

