import random
import datasets as ds
import itertools


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
    intersection_symbol = u'\u2229'
    union_symbol = u'\u222a'
    empty_symbol = u'\u2205'
    delta = u'\u0394'
    set1 = str(set_1).replace("'", '').replace("[", '(').replace(']', ')')
    set2 = str(set_2).replace("'", '').replace("[", '(').replace(']', ')')
    if op == 'union':
        output = set1 + ' ' + union_symbol + ' ' + set2 + ' = ' + str(set(set_1).union(set(set_2))).replace("'",
                                                                                                            '').replace(
            "{", '(').replace('}', ')')
        answer = str(set(set_1).union(set(set_2))).replace("'", '').replace("{", '(').replace('}', ')')

    elif op == 'intersection':
        output = set1 + ' ' + intersection_symbol + ' ' + set2 + ' = ' + str(
            set(set_1).intersection(set(set_2))).replace('set()', empty_symbol).replace("'", '').replace("{",
                                                                                                         '(').replace(
            '}', ')')
        answer = str(set(set_1).intersection(set(set_2))).replace('set()', empty_symbol).replace("'", '').replace("{",
                                                                                                                  '(').replace(
            '}', ')')
        if answer == empty_symbol:
            output = output + '  These two sets are disjoint.'

    elif op == 'difference':
        output = set1 + ' -' + ' ' + set2 + ' = ' + str(set(set_1).difference(set(set_2))).replace('set()',
                                                                                                   empty_symbol).replace(
            "'", '').replace("{", '(').replace('}', ')')
        answer = str(set(set_1).difference(set(set_2))).replace('set()', empty_symbol).replace("'", '').replace("{",
                                                                                                                '(').replace(
            '}', ')')

    elif op == 'cartesian':
        output = set1 + ' X ' + ' ' + set2 + ' = ' + str([(obj1, obj2) for obj1 in set_1 for obj2 in set_2]).replace(
            '[', '').replace(']', '')
        answer = str(set(set_1).difference(set(set_2))).replace('set()', empty_symbol).replace("'", '').replace("{",
                                                                                                                '(').replace(
            '}', ')')

    elif op == 'symmetric_difference':
        output = set1 + ' ' + delta + ' ' + set2 + ' = ' + str(
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




